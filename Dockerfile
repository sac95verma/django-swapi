FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y cron

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-crontab

# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Set environment variables for superuser creation
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin

RUN python manage.py createsuperuser --noinput
RUN python manage.py syncSwapiDevCommand


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["sh", "-c", "python manage.py crontab add && python manage.py runserver 0.0.0.0:8000"]