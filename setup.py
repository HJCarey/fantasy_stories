# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use Python Boilerplate to start
# simple, usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os

from setuptools import setup, find_packages

# Meta information
dirname = os.path.dirname(__file__)

# Save version and author to __meta__.py
path = os.path.join(dirname, 'gpt_stories', 'gpt_stories', '__meta__.py')
    
setup(
    # Basic info
    name='gpt_stories',
    version="0.0.1",
    author='Jake Carey',
    author_email='hjcarey@gmail.com',
    url='https://github.com/HJCarey/gpt_stories',
    description='Creates full stories from simple prompts.',
    long_description=open('README.md').read(),
    classifiers=[],

    # Packages and depencies    
    packages=find_packages(),
    install_requires=[
    ],

    extras_require={
        'dev': [
            'pytest',
        ],
    },

    # Data files
    package_data={
        'gpt_stories': [
            "*.yaml",
        ],
    },

    python_requires=">=3.11.0",
    include_package_data=True,
)