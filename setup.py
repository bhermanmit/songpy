#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='Distutils',
      version='1.0',
      description='Youtube Music Downloader',
      author='Chris Herman',
      author_email='crherman7@gmail.com',
      url='https://github.com/crherman7/songpy',
      packages=find_packages(),
      install_requires=['argparse', 'lxml'
          , 'requests', 'youtube-dl', 'eyed3'],
      entry_points={
          'console_scripts': [
              'songpy = src.__main__:main'
          ]
      }
      )
