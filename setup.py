#!/usr/bin/env python

from setuptools import setup

setup(
      name='Ebin',
      version='v0.6',
      description=('Spams a word of your choice on your terminal in rainbow colors.'),
      author='Vetrert and Ungentoo',
      author_email='vetrert@nigge.rs and gendev@protonmail.com',
      url='https://github.com/GNUPlusVet/Ebin',
      license='GPLv3',
      #packages=['ebin'],
      install_requires=[
        "termcolor",
    ],
      classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
],
)
