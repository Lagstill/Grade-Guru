from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str) -> List[str]:
    """Return requirements from requirements.txt file."""
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = 'MLProject',
    version = '0.1',
    packages = find_packages(),
    author = "Alagu Prakalya",
    author_email = "alagu.prakalya@gmail.com",
    install_requires = get_requirements('requirements.txt'),
          )

