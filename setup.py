from setuptools import setup

setup(
    name='seatfinder',
    version='0.0.1',
    url='https://github.com/soerface/py_seatfinder',
    description='Easy access to the data of the KIT seatfinder. '
                'This project is not affiliated in any way with the original author of https://www.seatfinder.de/',
    packages=['seatfinder'],
    install_requires=['requests', 'pandas', 'matplotlib'],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
