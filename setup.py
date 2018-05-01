from setuptools import setup, find_packages
from os.path import join, dirname
import number_to_string

setup(
    name='number_to_string',
    version=number_to_string.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    license='MIT',
    author='Andrey Berenda',
    author_email='berenda.andrey@gmail.com',
    url='https://github.com/berenda-andrey/ru_number_to_text',
)
