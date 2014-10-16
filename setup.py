
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='solcheck',
    description='ICPC Solution Validator',
    version='0.1',
    url='',
    license='Public domain',
    long_description=read('Readme.md'),
    py_modules=['solcheck'],
    install_requires = [],
    scripts=['solcheck.py'],
    )


