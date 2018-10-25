from setuptools import setup

setup(
    name='seatfinder',
    version='0.0.1',
    description='Easy access to the data of the KIT seatfinder. '
                'This project is not affiliated in any way with the original author of https://www.seatfinder.de/',
    packages=['seatfinder'],
    dependencies=['requests', 'pandas']
)
