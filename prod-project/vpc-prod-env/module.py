instance = ec2.Instance(self, "Instance",
    vpc=vpc,
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
    machine_image=ec2.MachineImage.latest_amazon_linux2023(),
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.VpcOrigin.with_ec2_instance(instance))
)

key_pair = ec2.KeyPair.from_key_pair_attributes(self, "KeyPair",
    key_pair_name="the-keypair-name",
    type=ec2.KeyPairType.RSA
)

vpc = ec2.Vpc(self, "TheVPC",
    ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16")
)

# Iterate the private subnets
selection = vpc.select_subnets(
    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
)

for subnet in selection.subnets:
    pass

import aws_cdk.aws_ec2 as ec2


vpc = ec2.Vpc(self, "Vpc",
    ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16")
)

vpc_connector = apprunner.VpcConnector(self, "VpcConnector",
    vpc=vpc,
    vpc_subnets=vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC),
    vpc_connector_name="MyVpcConnector"
)

apprunner.Service(self, "Service",
    source=apprunner.Source.from_ecr_public(
        image_configuration=apprunner.ImageConfiguration(port=8000),
        image_identifier="public.ecr.aws/aws-containers/hello-app-runner:latest"
    ),
    vpc_connector=vpc_connector
)
