from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='yayes',
      version='0.1',
      description='Repair erroneous entries in data streams while maintaining accuracy of overall trends.',
      url='https://github.com/hayesjosh/yayes',
      author='Greg Yannett & Josh Hayes',
      author_email='gsyann@berkeley.edu, hayesjosh@alumni.stanford.edu',
      license='MIT',
      packages='yayes',
      zip_safe=False,
      install_requires=['numpy','pandas'],
      classifiers=['Development Status :: 4-Beta',
                   'Programming Language :: Python'],
      keywords='yayes smoothing data error fill patching trend Greg Yannett Josh Hayes',
      include_package_data=True)