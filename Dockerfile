# Base image
FROM python:3.6-slim AS build
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app/
COPY ./strictdf_module /app
# Build the project
RUN python /app/setup.py bdist_wheel


# Base image
FROM python:3.6-slim

# Updating repository sources
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install -y python3-setuptools
#RUN apt-get install -y python3-dev

WORKDIR /tmp
COPY --from=build /app/dist/*.whl /tmp/wheel/
ADD ./jupyter /tmp
RUN pip install cytoolz==0.8
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install /tmp/wheel/*.whl

# Expose jupyter port
EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
