import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.custom-resources",
    "version": "1.2.0",
    "description": "Constructs for implementing CDK custom resources",
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
        "aws_cdk.custom_resources",
        "aws_cdk.custom_resources._jsii"
    ],
    "package_data": {
        "aws_cdk.custom_resources._jsii": [
            "custom-resources@1.2.0.jsii.tgz"
        ],
        "aws_cdk.custom_resources": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.2",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudformation~=1.2,>=1.2.0",
        "aws-cdk.aws-iam~=1.2,>=1.2.0",
        "aws-cdk.aws-lambda~=1.2,>=1.2.0",
        "aws-cdk.aws-sns~=1.2,>=1.2.0",
        "aws-cdk.core~=1.2,>=1.2.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
