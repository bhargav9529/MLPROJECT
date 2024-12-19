from setuptools import setup, find_packages
from typing import List

HYPEN = "-e ."
def req_packages(file_path:str)->List[str]:
    ##this will read the file 
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("/n","") for req in  requirements]
    if HYPEN in requirements:
        requirements.remove(HYPEN)
    return requirements


setup(
name="mlproject",
author="Bhargav",
author_email="vbnbhargav@gmail.com",
version="0.01",
description="demo pupose package creation",
packages=find_packages(),
requires=req_packages("requirements.txt")
)