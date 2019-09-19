from setuptools import setup, Extension

from os import path
this_directory = path.abspath(path.dirname("yayes"))
with open(path.join(this_directory, 'README-pypi.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(name='yayes',
      version='1.0.5',
      description='Repair erroneous entries in data streams while maintaining accuracy of overall trends.',
      url='https://github.com/hayesjosh/yayes',
      author='Greg Yannett & Josh Hayes',
      author_email='gsyann@berkeley.edu, hayesjosh@alumni.stanford.edu',
      license='MIT',
      packages=['yayes'],
      install_requires=['numpy','pandas'],
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python'],
      keywords='yayes smoothing data error fill patching trend Greg Yannett Josh Hayes',
      include_package_data=True,
      zip_safe=True,
      long_description=long_description,
      long_description_content_type='text/markdown')