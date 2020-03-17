FROM python:3.6-slim AS build
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app/
COPY ./strictdf_module /app
# Build the project
RUN python /app/setup.py bdist_wheel
