from aws_cdk import aws_sso as sso

cfn_application = sso.CfnApplication(self, "MyCfnApplication",
    application_provider_arn="applicationProviderArn",
    instance_arn="instanceArn",
    name="name",

    # the properties below are optional
    description="description",
    portal_options=sso.CfnApplication.PortalOptionsConfigurationProperty(
        sign_in_options=sso.CfnApplication.SignInOptionsProperty(
            origin="origin",

            # the properties below are optional
            application_url="applicationUrl"
        ),
        visibility="visibility"
    ),
    status="status",
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)

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

