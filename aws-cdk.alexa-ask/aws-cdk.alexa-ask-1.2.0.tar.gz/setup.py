import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.alexa-ask",
    "version": "1.2.0",
    "description": "The CDK Construct Library for Alexa::ASK",
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
        "aws_cdk.alexa_ask",
        "aws_cdk.alexa_ask._jsii"
    ],
    "package_data": {
        "aws_cdk.alexa_ask._jsii": [
            "alexa-ask@1.2.0.jsii.tgz"
        ],
        "aws_cdk.alexa_ask": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.2",
        "publication>=0.0.3",
        "aws-cdk.core~=1.2,>=1.2.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
