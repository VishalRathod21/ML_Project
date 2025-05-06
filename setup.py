from setuptools import setup, find_packages
from typing import List  # Import List from typing

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:  # Change list[str] to List[str]
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:  # Use the passed file_path
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ML Project",
    version="0.1.0",
    author="Vishal Rathod",
    author_email="vr3204917@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
