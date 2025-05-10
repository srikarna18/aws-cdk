from aws_cdk import (
    Stack,
    aws_organizations as organizations,
)
from constructs import Construct

class ControlTowerScpStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
      
        scp = organizations.CfnPolicy(
            self, "DenyS3PublicAcl",
            name="DenyS3PublicAccess",
            description="Denies public S3 bucket/object ACLs",
            type="SERVICE_CONTROL_POLICY",
            content={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "DenyS3PublicRead",
                        "Effect": "Deny",
                        "Action": ["s3:PutBucketAcl", "s3:PutObjectAcl"],
                        "Resource": "*",
                        "Condition": {
                            "StringEquals": {
                                "s3:x-amz-acl": "public-read"
                            }
                        }
                    }
                ]
            }
        )
      
        organizations.CfnPolicyAttachment(
            self, "AttachScpToOu",
            policy_id=scp.ref,
            target_id="ou-xxxx-yyyyyyyy"  # <- Replace with real OU ID
        )
