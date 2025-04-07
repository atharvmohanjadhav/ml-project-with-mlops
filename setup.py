from setuptools import find_packages,setup
from typing import List

"""
setup.py is the traditional method for defining package metadata and dependencies. 
It uses setuptools or distutils to specify how the package should be built and installed. 
The file typically includes information like the package name, version, author, dependencies, etc.

"""

e_dot = "-e ."   

def get_requirements(filepath:str)-> List[str]:
    """
    this function will return list of requirements
    """
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements
    
setup(
    name="mlops-project",
    version="0.0.1",
    author="Atharv Mohan Jadhav",
    author_email="atharvjadhav2910@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")

)