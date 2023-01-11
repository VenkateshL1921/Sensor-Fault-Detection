# script which will ensure that sensor folder can be installed as libraries
from setuptools import find_packages, setup


def get_requirements():
    """
    This function will return list of requirements
    """

    requirement_list = []
    # read req.txt file and append each req in above variable

    return requirement_list


setup(

    name="Sensor",
    version="0.0.1",
    author="venky",
    author_email="venkyslotlikar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
