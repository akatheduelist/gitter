from setuptools import find_packages, setup

setup(
  name='gitter',
  packages=find_packages(include=['gitter']),
  version='0.1.0',
  description='git gud with gitter',
  author='akatheduelist',
  install_requires=['requests'],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  test_suite='tests'
)