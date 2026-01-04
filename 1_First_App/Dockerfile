# Pull base image for Python
FROM python:3.8-slim

# Set working directory in the Image
WORKDIR /app

# Copy the current directory contents at /app in the Image
# COPY app.py /app  
# COPY Dockerfile /app
COPY . /app
# source /destination 


# Run the application
CMD ["python", "app.py"] 
# only run when container is initiated 


# run docker build -t first_app (in the terminal )
# docker run ----> runs the container
# docker run --name first_python_cotainer first_python_app
#                     run this container    which image            
# docker build ---->  builds the image
