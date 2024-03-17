from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements( file_path:str)->List[str]:
    '''
    this fnct return list of requirments 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #[req.replace("\n","") for req in requirements]
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
     name='mlproject',
     version='0.01',
     author='k_tutor',
     author_email='kwilu6@gmail.com',
     packages=find_packages(),
     install_requires=get_requirements('requirements.txt') #['pandas', 'numpy', 'seasborn']


)