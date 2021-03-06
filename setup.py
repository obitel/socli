try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
from os import path
from sys import exit,version
import sys
if version < '1.0.0':
    print("Python 1 is not supported...")
    sys.exit(1)

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long = f.read()

setup(
    name='socli',
    packages=["socli"],
    entry_points = {"console_scripts": ['socli = socli.socli:main']},
    install_requires=['BeautifulSoup4','requests'],
    requires=['BeautifulSoup4','requests'],
    version='2.1',
    url='http://www.github.com/gautamkrishnar/socli',
    keywords="stack overflow cli",
    license='BSD',
    author='Gautam krishna R',
    author_email='r.gautamkrishna@gmail.com',
    description='Stack overflow commnand line interface. SoCLI allows you to search and browse stack overfow from the terninal.',
    long_description=long
    )