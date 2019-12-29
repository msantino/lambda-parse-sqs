import glob
import imp
import io
import os
from os import path
from setuptools import setup, find_packages, Extension
import sys

MYDIR = path.abspath(os.path.dirname(__file__))

cmdclass = {}
ext_modules = []

setup(
    name='lambda_parse_sqs',  
    version='0.2.1',
    author="Marcelo Santino",
    author_email="eu@marcelosantino.com.br",
    description="Parse SQS messages from lambda triggered SQS subscription",
    url='https://github.com/msantino/lambda-parse-sqs',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )