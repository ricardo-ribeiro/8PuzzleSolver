from distutils.core import setup
from setuptools import find_packages

setup(
    name='Puzzle',
    version='0.0.2',
    packages= find_packages(),
    url='ricardoribeiro.uk',
    license='Open Source',
    author='Ricardo',
    author_email='ricardo.lcmr@gmail.com',
    description='8 Puzzle solver with Nielson Manhattan Out of Row Heuristics and AStar Algorithm -- CPU Model -- can take hours to compute',
    entry_points={
        'console_scripts': [
            'Puzzle=Main.Main',
        ],
    }
)
