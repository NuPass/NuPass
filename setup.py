"""
    setup.py
    ~~~~~~~~

    Package setup file for nupass.

    :copyright: (c) 2021 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(name='nupass',
      version='1.0.0',
      description='Generate readable, typable passwords',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
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
      entry_points={
          'console_scripts': [
              'nupass = nupass.script:main',
          ],
      },
      include_package_data=True,
      zip_safe=False)
