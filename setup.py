from setuptools import setup, find_packages

setup(
    name = "myparkage",
    version= "0.1",
    parkage = find_packages(exclude = ["tests*"]),
    licence = "MIT",
    description= 'EDSA example python parkage',
    long_description=open('README.md').read(),
    install_requires= ['numpy'],
    url='https://github.com',
    author='fumani',
    author_email='fumanithibela13@gmail.com'
)