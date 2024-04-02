from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setup(
    name='firstPackage',
    version='0.1.0',
    author='NekouDfrm',
    author_email='nekou.workcpe@gmail.com',
    description='working on packaging in python',
    long_description=open('README.txt').read(),
    python_requires='>3.10',
    packages=['PyPackage'],
    install_requires=required
)