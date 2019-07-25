import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-elasticloadbalancing",
    "version": "1.2.0",
    "description": "CDK Constructs for AWS ElasticLoadBalancing",
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
        "aws_cdk.aws_elasticloadbalancing",
        "aws_cdk.aws_elasticloadbalancing._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_elasticloadbalancing._jsii": [
            "aws-elasticloadbalancing@1.2.0.jsii.tgz"
        ],
        "aws_cdk.aws_elasticloadbalancing": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.2",
        "publication>=0.0.3",
        "aws-cdk.aws-ec2~=1.2,>=1.2.0",
        "aws-cdk.core~=1.2,>=1.2.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
