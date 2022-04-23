"""Setup script for mitype."""
from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1.0',
    packages=find_packages(include=['typing_meter', 'typing_meter.*'])
)
