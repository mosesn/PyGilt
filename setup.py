import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyGilt",
    version = "0.0.1",
    author = "Moses Nakamura",
    author_email = "innythm@gmail.com",
    description = ("Gilt API Client."),
    license = "BSD",
    keywords = "Gilt",
    url = "https://github.com/mnn2104/PyGilt",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
