# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"', open("csv2keychain.py").read(), re.M
).group(1)

with open("README.md") as f:
    long_description = f.read()

setup(
    name="cmdline-csv2keychain",
    packages=["csv2keychain"],
    entry_points={"console_scripts": ["csv2keychain = csv2keychain:main"]},
    version=version,
    description="Tool for adding exported credentials from Chrome to the macOS keychain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nikita Tarasov",
    author_email="mail@ntarasov.ru",
    url="https://github.com/nntarasov/csv2keychain",
)
