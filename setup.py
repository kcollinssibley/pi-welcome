#!/usr/bin/env python
from setuptools import setup

setup(
    name='pi-welcome',
    version='0.1.0',
    description='A morning information dump including MBTA predictions, '
    'Weather, etc.',
    author='Kofi Collins-Sibley',
    author_email='colko818@gmail.com',
    url='https://github.com/kcollinssibley/pi-welcome',
    license='MIT',
    packages=['pi_welcome'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'app = pi_welcome.app:main'
        ]
    }
)
