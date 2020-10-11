#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='drugwars',
    version='1.2.1',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='The 80s DOS game re-written in Python',
    long_description=open('./README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/Drugwars',
    packages=find_packages(),
    install_requires=[
        'terminaltables',
        'requests'
    ],
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'drugwars = drugwars.__main__:main',
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Games/Entertainment :: Turn Based Strategy'
    ]
)
