# The first line contains the image that we are inheriting our file of.
# We are gonna be using the python 3.7 alpine image, the lighweight Docker based on
# python image.
FROM python:3.7-alpine

LABEL maintainer="Github: joaovmvale"

# Unbuffured python environment -> Doesn't allow python to buffer outputs
ENV PYTHONUNBIFFERED 1

# Installing dependecies from the local file and storing it on Docker container
COPY ./requirements.txt /requirements.txt
# Running and installing the requirements in the container
RUN pip install -r /requirements.txt

# Creating an empty folder on container
RUN mkdir /app
# Switching the working directory
WORKDIR /app
# Copying the local app folder to the container app folder
COPY ./app /app

# Creating a user to run the application
RUN adduser -D user
# Switching to the created user
USER user
# ** The user is created for security purposes, because if you don't create it,
# the default iser is the root user.