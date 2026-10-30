# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application source code into the container
COPY app/ /app/app/
COPY tests/ /app/tests/

# Command to run when the container starts
CMD ["python", "app/app.py"]