FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py crontab add

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]