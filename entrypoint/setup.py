#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="entrypoint",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "entrypoint=entrypoint.cli:main",
        ],
    },
    install_requires=["yamllint ~= 1.0"],
)
