
from setuptools import find_packages,setup

from typing import List


def get_requirements()->List[str]:

    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            for l in lines:
                l=l.strip()
                if l and l!='-e .':
                    requirements_lst.append(l)

    except FileNotFoundError:
        print("requirements.txt doesnt exist")

    return requirements_lst


# print(get_requirements())

#### *** setup metadata

setup(
    name='project-mlops',
    version="0.0.1",
    author="Aritra Mandal",
    author_email='maritra36@gmail.com',
    packages=find_packages(),
    ## find_packages() is a helper function from setuptools that automatically finds all the Python packages in your project so you don't have to list them manually
    ## manual listing looks like this:
    ## setup(
    #     ...
    #     packages=[
    #         "networksecurity",
    #         "networksecurity.pipeline",
    #         "networksecurity.utils",
    #         "networksecurity.components"
    #     ]
    # )
    install_requires=get_requirements()
)