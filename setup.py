from setuptools import find_packages,setup
from typing import List

e_dot = "-e ."   # this for, when we run requirements.txt it will automatically triggers setup.py
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