#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-mstranslate',
    version='0.1.0',
    description="Text-To-Speech with MStranslate",
    long_description=readme + '\n\n' + history,
    author="Areski Belaid",
    author_email='areski@gmail.com',
    url='https://github.com/newfies-dialer/python-mstranslate',
    packages=[
        'mstranslate',
    ],
    package_dir={'mstranslate':
                 'mstranslate'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='mstranslate',
    entry_points={
        'console_scripts': [
            'mstranslate = mstranslate.command_line:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License (MIT)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)