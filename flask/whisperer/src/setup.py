from setuptools import setup, find_packages

setup(name='whisperer',
      version='0.1',
      description='A Flask micro-service that receives text whispers from users'
                  'and triggers a kafka event ',
      url='https://github.com/hamshif/whisperer.git',
      author='gbar',
      author_email='hamshif@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['flask'],
      extras_require={
            'test': [
                  'requests'
            ],
      }
      )
