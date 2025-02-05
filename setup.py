import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
DESCRIPTION = "scTenifoldpy"

PKGS = find_packages()
PKG_NAME = "scTenifoldpy"
PKG_VERSION = '0.1.3'

MAINTAINER = 'Yu-Te Lin'
MAINTAINER_EMAIL = 'qwerty239qwe@gmail.com'

PYTHON_REQUIRES = ">=3.7"
URL = "https://github.com/qwerty239qwe/scTenifoldpy"

LICENSE = "MIT"
CLFS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

INSTALL_REQUIRES = [
        "pandas",
        "numpy",
        "scipy",
        "setuptools",
        "typer",
        "PyYAML",
        "ray",
        "scikit-learn",
        "tensorly",
        "requests",
        "seaborn",
        "matplotlib",
        "networkx",
        "scanpy",
        "protobuf",
    ]

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=PKG_VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    license=LICENSE,
    classifiers=CLFS,
    packages=PKGS,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        "console_scripts": [
            "scTenifold=scTenifold.__main__:app",
        ]
    },
)