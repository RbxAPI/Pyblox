from distutils.core import setup
import setuptools
setup(
  name = 'pyblox3',
  packages = ['pyblox'],
  version = '2.4.1',
  license='MIT',       
  description = 'An API wrapper for Roblox written in Python.',
  long_description = '''
  An API wrapper for Roblox written in Python.
  Light-weight version that's aimed to be stable while providing basic functionality.
  Archived version. 
  ''',
  url = 'https://github.com/RbxAPI/Pyblox/tree/master',
  author = 'Sanjay Bhadra (Sanjay-B)',        
  author_email = 'sanjay2003rbx@gmail.com',
  keywords = ['api', 'roblox', 'roblox-api', 'python-api', 'pyblox', 'pyblox3'],
  install_requires=['requests','beautifulsoup4==4.6.3','html5lib'], # Replace with requirements.txt
  classifiers=[
    'Development Status :: 3',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: MIT License',  
    'Programming Language :: Python :: 3.7',
  ],
)
