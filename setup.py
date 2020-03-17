import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements_file = os.path.join(os.path.curdir,
                                 'strictdf', 'requirements.txt')

with open(requirements_file) as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="strictdf",
    version="0.0.1",
    author="Damian Bourdin",
    author_email="damian.bourdin@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbourdin/strictdf/",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
