# -*- coding: utf-8 -*-

import os
from codecs import open
from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "A git extension which provides commands for working according Git-Flow easily & safely in your repository."

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r") as f:
    readme = f.read()

with open(os.path.join(here, "requirements.txt"), "r") as f:
    requires = f.read()

setup(
    name="github-flow",
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    author="ShakedBraimok (Shaked Braimok Yosef)",
    author_email="shaked.braimok.yosef@gmail.com",
    url="https://github.com/ShakedBraimok/github-flow",
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    license="GPL",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "git-flow=src.github_flow:main",
        ],
        "gui_scripts": [],
    }
)
