# Use the official Python base image
FROM python:3.9-bullseye

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

# Copy the application code
COPY . .

RUN adduser dockuser
RUN chown dockuser:dockuser -R /app/
USER dockuser

# Expose the port the app will run on
EXPOSE 8000