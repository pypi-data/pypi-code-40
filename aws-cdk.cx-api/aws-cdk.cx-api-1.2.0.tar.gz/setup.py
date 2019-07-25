import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.cx-api",
    "version": "1.2.0",
    "description": "Cloud executable protocol",
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
        "aws_cdk.cx_api",
        "aws_cdk.cx_api._jsii"
    ],
    "package_data": {
        "aws_cdk.cx_api._jsii": [
            "cx-api@1.2.0.jsii.tgz"
        ],
        "aws_cdk.cx_api": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.2",
        "publication>=0.0.3"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
