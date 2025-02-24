from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        # so when we fo file_obj.readlines(), \n comes. thats why we are removing it

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        # We have put '-e .' in requiremets.txt just to trigger setup.py with requirements.txt

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Vedant',
    author_email='vedanttvs1012@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)
