import aws_cdk.aws_identitystore as identitystore

from aws_cdk import aws_identitystore as identitystore

cfn_group = identitystore.CfnGroup(self, "MyCfnGroup",
    display_name="displayName",
    identity_store_id="identityStoreId",

    # the properties below are optional
    description="description"
)

from aws_cdk import aws_identitystore as identitystore

cfn_group_membership = identitystore.CfnGroupMembership(self, "MyCfnGroupMembership",
    group_id="groupId",
    identity_store_id="identityStoreId",
    member_id=identitystore.CfnGroupMembership.MemberIdProperty(
        user_id="userId"
    )
)

from aws_cdk import aws_identitystore as identitystore

member_id_property = identitystore.CfnGroupMembership.MemberIdProperty(
    user_id="userId"
)

from aws_cdk import aws_identitystore as identitystore

cfn_group_membership_props = identitystore.CfnGroupMembershipProps(
    group_id="groupId",
    identity_store_id="identityStoreId",
    member_id=identitystore.CfnGroupMembership.MemberIdProperty(
        user_id="userId"
    )
)

from aws_cdk import aws_identitystore as identitystore

cfn_group_props = identitystore.CfnGroupProps(
    display_name="displayName",
    identity_store_id="identityStoreId",

    # the properties below are optional
    description="description"
)

