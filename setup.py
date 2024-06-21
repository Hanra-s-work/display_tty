"""
File containing the required information to successfully build a python package
"""

import setuptools

with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
    long_description = fh.read()

setuptools.setup(
    name='display_tty',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=[
        "colorlog==6.8.2",
        "logging==0.4.9.6"
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="A module that allows you to display text with a few boilers (i.e. put your text in a square for titles)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/disp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
