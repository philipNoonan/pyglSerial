#!/usr/bin/env python

"""The setup script."""

import os
from setuptools import setup, find_packages

requirements = [
    'glfw',
    'PyOpenGL',
    'serial',
    'imgui',
    'numpy'
]

setup(
    author='PN',
    author_email='philip.noonan@hypervisionsurgical.com',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pyglSerial=pyglserial.pyglSerial:main',
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    name='pyglflow',
    packages=find_packages(include=['pyglserial', 'pyglserial.*']),
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/philipNoonan/pyglSerial',
    version='0.1.0',
    zip_safe=False,
)
