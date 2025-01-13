# Using Python 3.12.2 as the base image
FROM python:3.12.2-slim-bullseye                              
# Ensures that Python output is sent straight to the terminal (e.g., for logging)
ENV PYTHONUNBUFFERED=1                          
# variable for port 8080 
ENV PORT 8080                                   
# Set the working directory to /app
WORKDIR /app                                    
# Copy the current directory contents into the container at /app
COPY . /app/                                    
# Upgrade pip to the latest version
RUN pip install --upgrade pip                   
# Install the required packages from requirements.txt
RUN pip install -r requirements.txt             

#CMD python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver

# Run app with gunicorn command
CMD gunicorn sysapp.wsgi:application --bind 0.0.0.0::"${PORT}"  
# --workers 3 --threads 2 --timeout 120 --log-level info --log-file -


# Expose the port the contanerized app runs on
EXPOSE ${PORT}                                  
