from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkHaVpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC with 2 AZs, 1 NAT Gateway, public and private subnets
        vpc = ec2.Vpc(self, "HaVpc",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )

        # Security Group allowing SSH
        sg = ec2.SecurityGroup(self, "InstanceSG",
            vpc=vpc,
            description="Allow SSH",
            allow_all_outbound=True
        )
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH")

        # Amazon Linux 2 AMI
        ami = ec2.MachineImage.latest_amazon_linux()

        # Launch EC2 Instances in each PUBLIC subnet for HA
        public_subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnets
        for i, subnet in enumerate(public_subnets):
            ec2.Instance(self, f"PublicInstance{i}",
                vpc=vpc,
                instance_type=ec2.InstanceType("t3.micro"),
                machine_image=ami,
                security_group=sg,
                vpc_subnets=ec2.SubnetSelection(subnets=[subnet]),
            )
