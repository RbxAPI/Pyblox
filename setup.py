from distutils.core import setup
setup(
  name = 'pyblox3',
  packages = ['pyblox', 'robloxapi.utils', 'robloxapi.classes'],
  version = '4',
  license='MIT',       
  description = 'A Python wrapper for roblox',
  long_description = '''
  Just another wrapper for the roblox api. 
  github: https://github.com/iranathan/robloxapi
  docs: https://robloxapi.readthedocs.io/en/latest/ (not the full package is documented will be soon.)
  
  There is also an async version on the github.
  ''',
  url = 'https://github.com/iranathan/robloxapi',
  author = 'Iranathan',                
  author_email = 'iranathan8@gmail.com',
  keywords = ['python_roblox', 'roblox', 'robloxapi'],
  install_requires=[            
          'requests',
          'beautifulsoup4'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
  ],
)