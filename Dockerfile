# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Create a working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Set the command to start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
