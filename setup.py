# -*- coding: utf-8 -*-
"""Setup file for the package"""
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='saveme',
    description='OSX Menu Bar for AWS-Vault Metadata Server (via launchctl)',
    author='Marcus Young',
    author_email='myoung34@my.apsu.edu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['saveme'],
    version='0.0.2',
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['*.icns', '*.pt', 'vendor']},
    install_requires=[
      'altgraph==0.17',
      'chameleon==3.9.0',
      'click==7.1.2',
      'macholib==1.14',
      'modulegraph==0.18',
      'py2app==0.23',
      'pyobjc-core==7.1',
      'pyobjc-framework-cocoa==7.1',
      'rumps==0.3.0',
      'shellescape==3.8.1',
    ],
    entry_points={
        'console_scripts': [
            'saveme=saveme.cli:run',
        ],
    },
)
