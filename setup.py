from setuptools import setup, find_packages
setup(
  name="raidwrap",
  version="0.2",
  description="wrapper utility for all those confusing RAID configurator apps",
  author="Jeremy Hanmer",
  author_email="jeremy@dreamhost.com",
  url="http://github.com/fzylogic/raidwrap",
  license="Apache2",
  entry_points={
      'console_scripts': [
          'raidwrap=raidwrap.cli:main'
          ]
      },
  packages=find_packages(),
)
