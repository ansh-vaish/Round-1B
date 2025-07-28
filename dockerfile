# Use official Python base image (not slim) to avoid dependency issues
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all local files to the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the main script
CMD ["python", "extract.py"]
