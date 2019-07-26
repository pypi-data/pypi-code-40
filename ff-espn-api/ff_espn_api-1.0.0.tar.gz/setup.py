from setuptools import setup

setup(
    name='ff_espn_api',
    packages=['ff_espn_api'],
    version='1.0.0',
    author='Christian Wendt',
    description='Fantasy Football ESPN API',
    install_requires=['requests>=2.0.0,<3.0.0'],
    test_suite='nose.collector',
    tests_require=['nose', 'requests_mock'],
    url='https://github.com/cwendt94/ff-espn-api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)