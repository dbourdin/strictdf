import os
import setuptools

_setup_dir = os.path.dirname(__file__)
_readme_file = os.path.join(_setup_dir, 'README.md')
with open(_readme_file) as f:
    _long_description = f.read()

_requirements_file = os.path.join(_setup_dir, 'strictdf', 'requirements.txt')

with open(_requirements_file) as f:
    _requirements = f.read().splitlines()

setuptools.setup(
    name="strictdf",
    version="0.0.1",
    author="Damian Bourdin",
    author_email="damian.bourdin@gmail.com",
    description="",
    long_description=_long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbourdin/strictdf/",
    packages=setuptools.find_packages(),
    install_requires=_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
