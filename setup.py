from setuptools import setup, find_packages

with open('requirements.txt','r') as f:
	req = f.read().splitlines()

version = '0.1.0'

setup(
	name = 'drootoo_load_forecasting',
	version=version,
	install_requires=req,
	author='Harsh Munshi',
	author_email='harshmunshi03@gmail.com',
	packages=find_packages()
	)
