#find_packages will automatically find all required packages use in machine learning proj in the directory we created
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

#Basically meta data about the entire project
setup(

    name='mlproject1',
    version='0.0.1',
    author='Qaiser Javed',
    author_email='qasjaved@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt')


)