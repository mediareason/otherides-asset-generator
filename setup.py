#!/usr/bin/env python3
"""
Setup script for OTHERIDES Asset Generator
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="otherides-asset-generator",
    version="1.0.0",
    author="MediaReason",
    author_email="contact@mediareason.com",
    description="AI-powered vehicle generator for the OTHERIDES NFT collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mediareason/otherides-asset-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["data/*.json"]
    },
    entry_points={
        "console_scripts": [
            "otherides-generate=otherides_generator:main",
        ],
    },
    keywords="nft, ai, art-generation, otherides, metaverse, yuga-labs, otherside",
    project_urls={
        "Bug Reports": "https://github.com/mediareason/otherides-asset-generator/issues",
        "Source": "https://github.com/mediareason/otherides-asset-generator",
        "Documentation": "https://github.com/mediareason/otherides-asset-generator#readme",
    },
)