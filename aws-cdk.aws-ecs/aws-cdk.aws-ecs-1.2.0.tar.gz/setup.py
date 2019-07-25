import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-ecs",
    "version": "1.2.0",
    "description": "The CDK Construct Library for AWS::ECS",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_ecs",
        "aws_cdk.aws_ecs._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_ecs._jsii": [
            "aws-ecs@1.2.0.jsii.tgz"
        ],
        "aws_cdk.aws_ecs": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.2",
        "publication>=0.0.3",
        "aws-cdk.aws-applicationautoscaling~=1.2,>=1.2.0",
        "aws-cdk.aws-autoscaling~=1.2,>=1.2.0",
        "aws-cdk.aws-autoscaling-hooktargets~=1.2,>=1.2.0",
        "aws-cdk.aws-certificatemanager~=1.2,>=1.2.0",
        "aws-cdk.aws-cloudformation~=1.2,>=1.2.0",
        "aws-cdk.aws-cloudwatch~=1.2,>=1.2.0",
        "aws-cdk.aws-ec2~=1.2,>=1.2.0",
        "aws-cdk.aws-ecr~=1.2,>=1.2.0",
        "aws-cdk.aws-ecr-assets~=1.2,>=1.2.0",
        "aws-cdk.aws-elasticloadbalancing~=1.2,>=1.2.0",
        "aws-cdk.aws-elasticloadbalancingv2~=1.2,>=1.2.0",
        "aws-cdk.aws-iam~=1.2,>=1.2.0",
        "aws-cdk.aws-lambda~=1.2,>=1.2.0",
        "aws-cdk.aws-logs~=1.2,>=1.2.0",
        "aws-cdk.aws-route53~=1.2,>=1.2.0",
        "aws-cdk.aws-route53-targets~=1.2,>=1.2.0",
        "aws-cdk.aws-secretsmanager~=1.2,>=1.2.0",
        "aws-cdk.aws-servicediscovery~=1.2,>=1.2.0",
        "aws-cdk.aws-sns~=1.2,>=1.2.0",
        "aws-cdk.aws-sqs~=1.2,>=1.2.0",
        "aws-cdk.aws-ssm~=1.2,>=1.2.0",
        "aws-cdk.core~=1.2,>=1.2.0",
        "aws-cdk.cx-api~=1.2,>=1.2.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
