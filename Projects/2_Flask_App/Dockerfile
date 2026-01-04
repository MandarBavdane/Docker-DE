# Pull base image for Python
FROM python:3.8-slim

# Set working directory in the Image
WORKDIR /app

# Copy the requirements file into the image
# COPY requirements.txt /app/requirements.txt

# Copy everything needed from the current directory to install dependencies
# COPY . /app
COPY . .

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt


# Run the application
CMD ["python", "app.py"] 
