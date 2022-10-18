import os
import setuptools
root = os.path.dirname(os.path.abspath(__file__))
setuptools.setup(
    name             = 'package',
    description      = 'A Simple Package',
    packages         = setuptools.find_packages(),
)