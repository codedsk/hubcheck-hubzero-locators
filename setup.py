from setuptools import setup, find_packages

setup(name='hubcheck-hubzero-locators',
      version='1.0.0',
      description='hubcheck page object and locator settings for hubzero',
      author='Derrick Kearney',
      author_email='telldsk at gmail dot com',
      packages = find_packages(),
#      install_requires=['hubcheck>=1.0.0',
#                       ],
      include_package_data=True,
     )
