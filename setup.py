#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import ast
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("src/__init__.py", "rb") as f:
    VERSION = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

here = Path(__file__).parent.resolve()


def read(name):
    return Path(here, name).read_text(encoding="utf-8")


OPTIONAL = [
    "nest_asyncio",
]

TESTING = [
    # NOTE: pytest introduced some breaking changes
    "pytest==7.1.*",
    "pytest-cov",
    # TODO: update config so coveralls 3 works
    "coveralls<3",
    "flake8",
]

# packages needed for development
DEV = ["twine", "invoke", "pkgmt"]

DESCRIPTION = (
    "Write maintainable, project for solving Sudoku problems. "
)

setup(
    name="sudoku-solver",
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Yevhenii",
    author_email="senusheugen@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # https://pypi.org/classifiers/
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[

    ],
    extras_require={
        "all": OPTIONAL,
        "dev": OPTIONAL + TESTING + DEV,
    },
)
