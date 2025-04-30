from setuptools import setup, find_packages

setup(
    #this will be the package name you will see in pip list
    name = 'froglib', 
    #some version number you may wish to add - increment this after every update
    version='1.0', 
    package_dir = {"": "src"},  
    packages=find_packages(where="src")
)