from distutils.core import setup
setup(
  name = 'pyblox3',
  packages = ['pyblox', 'robloxapi.utils', 'robloxapi.classes'],
  version = '3.0.0',
  license='MIT',       
  description = 'An API wrapper for Roblox written in Python.',
  long_description = '''
  An API wrapper for Roblox written in Python.
  Full async/non-blocking I/O architecture aiming towards 100% API coverage.
  ''',
  url = 'https://github.com/RbxAPI/Pyblox/tree/nightly_build',
  author = 'Sanjay Bhadra (Sanjay-B)',                
  author_email = 'n/a',
  keywords = ['api', 'roblox', 'roblox-api', 'python-api', 'pyblox', 'pyblox3'],
  install_requires=['requests', 'aiohttp', 'asyncio', 'requests_async','beautifulsoup4'], # Replace with requirements.txt
  classifiers=[
    'Development Status :: 3',      

    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',

    'License :: MIT License',  
    'Programming Language :: Python :: 3.7',
  ],
)