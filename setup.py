#!/usr/bin/env python

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = ""
# doclink = """
# Documentation
# -------------

# The full documentation is at http://codemeta_bootstrap.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
authors = open('AUTHORS.rst').read()

setup(
    name='codemeta_bootstrap',
    version='0.1.0',
    description='"Bootstrap CodeMeta jsonld from a git repository"',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Jonathan Sick',
    author_email='jonathansick@mac.com',
    url='https://github.com/jonathansick/codemeta_bootstrap',
    packages=[
        'codemeta_bootstrap',
    ],
    package_dir={'codemeta_bootstrap': 'codemeta_bootstrap'},
    include_package_data=True,
    install_requires=[
        # 'jsonschema'
    ],
    license='MIT',
    zip_safe=False,
    keywords='codemeta_bootstrap',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
    ],
)
