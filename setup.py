import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='seatfinder',
    version='1.0.0',
    url='https://github.com/soerface/py_seatfinder',
    description='Easy access to the data of the KIT seatfinder. '
                'This project is not affiliated in any way with the original author of https://www.seatfinder.de/',
    long_description=read('README.md'),
    packages=['seatfinder'],
    install_requires=['requests', 'pandas', 'matplotlib'],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
