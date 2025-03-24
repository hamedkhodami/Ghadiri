# Use the official Python image from Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /django_app/

# Copy the requirements file into the container
ADD ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r ./requirements.txt

# Change the working directory
WORKDIR /django_app/src

# Copy the rest of the working directory contents into the container
ADD ./src ./

# Specify the entrypoint command to run on container start
ENTRYPOINT ["/bin/sh", "-c" , "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 config.wsgi"]