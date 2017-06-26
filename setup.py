from setuptools import setup

setup(name='nupass',
	  version='0.2',
	  description='Generate readable, typable passwords',
	  classifiers=[
	    'Development Status :: 4 - Beta',
	    'Programming Language :: Python :: 2.7',
	    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
	  ],
	  url='https://github.com/nupass/nupass',
	  author='Sean Callaway',
	  author_email='seancallaway@gmail.com',
	  license='GPLv2',
	  packages=['nupass'],
	  zip_safe=False)