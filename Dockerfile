# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY voting_app.py .

# Run the Python script when the container starts
CMD ["python", "voting_app.py"]

