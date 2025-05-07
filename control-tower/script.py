import aws_cdk.aws_controltower as controltower

from aws_cdk import aws_controltower as controltower

# value: Any

cfn_enabled_baseline = controltower.CfnEnabledBaseline(self, "MyCfnEnabledBaseline",
    baseline_identifier="baselineIdentifier",
    baseline_version="baselineVersion",
    target_identifier="targetIdentifier",

    # the properties below are optional
    parameters=[controltower.CfnEnabledBaseline.ParameterProperty(
        key="key",
        value=value
    )],
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)


from aws_cdk import aws_controltower as controltower

# value: Any

cfn_enabled_baseline_props = controltower.CfnEnabledBaselineProps(
    baseline_identifier="baselineIdentifier",
    baseline_version="baselineVersion",
    target_identifier="targetIdentifier",

    # the properties below are optional
    parameters=[controltower.CfnEnabledBaseline.ParameterProperty(
        key="key",
        value=value
    )],
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)


from aws_cdk import aws_controltower as controltower

# value: Any

cfn_enabled_control = controltower.CfnEnabledControl(self, "MyCfnEnabledControl",
    control_identifier="controlIdentifier",
    target_identifier="targetIdentifier",

    # the properties below are optional
    parameters=[controltower.CfnEnabledControl.EnabledControlParameterProperty(
        key="key",
        value=value
    )],
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)


from aws_cdk import aws_controltower as controltower

# value: Any

cfn_enabled_control_props = controltower.CfnEnabledControlProps(
    control_identifier="controlIdentifier",
    target_identifier="targetIdentifier",

    # the properties below are optional
    parameters=[controltower.CfnEnabledControl.EnabledControlParameterProperty(
        key="key",
        value=value
    )],
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)



from aws_cdk import aws_controltower as controltower

# manifest: Any

cfn_landing_zone = controltower.CfnLandingZone(self, "MyCfnLandingZone",
    manifest=manifest,
    version="version",

    # the properties below are optional
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)


from aws_cdk import aws_controltower as controltower

# manifest: Any

cfn_landing_zone_props = controltower.CfnLandingZoneProps(
    manifest=manifest,
    version="version",

    # the properties below are optional
    tags=[CfnTag(
        key="key",
        value="value"
    )]
)

