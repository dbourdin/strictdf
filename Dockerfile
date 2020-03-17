# Base image
FROM python:3.6-slim AS build

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app/
COPY ./strictdf_module /app

# Install dependencies to run tests
RUN pip install --upgrade pip
RUN pip install -r /app/strictdf/requirements.txt

# Run tests
RUN coverage run --source=/app/strictdf -m pytest

# Generate html report
RUN coverage html

# Build the project
RUN python /app/setup.py bdist_wheel


# Base image
FROM python:3.6-slim

# Updating repository sources
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install -y python3-setuptools

# Set the working directory to /tmp
WORKDIR /tmp

# Copy built wheel dependency and report.html
COPY --from=build /app/dist/*.whl /tmp/strictdf/
COPY --from=build /app/htmlcov /tmp/coverage

# Add jupyter notebook files to container
ADD ./jupyter /tmp

# Install dependencies
RUN pip install cytoolz==0.8
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install /tmp/strictdf/*.whl

# Setting up volumes
VOLUME ["/tmp/data", "/tmp/notebook"]

# Expose jupyter port
EXPOSE 8888

# Run jupyter notebook
CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
