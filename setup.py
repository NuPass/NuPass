"""
    setup.py
    ~~~~~~~~

    Package setup file for nupass.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from setuptools import setup

setup(name='nupass',
      version='0.2.1',
      description='Generate readable, typable passwords',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'],
      url='https://github.com/nupass/nupass',
      author='Sean Callaway',
      author_email='seancallaway@gmail.com',
      license='GPLv2',
      packages=['nupass'],
      scripts=['bin/nupass'],
      include_package_data=True,
      zip_safe=False)
