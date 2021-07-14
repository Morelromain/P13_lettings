# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

EXPOSE 8000

# Create /app directory
RUN mkdir -p /app
WORKDIR /app

# set environment variables AJOUT!!!!
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=0
ENV PORT 8000
ENV DJANGO_SECRET_KEY="fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

# Install  requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app.
COPY . /app/

# Collect all static files in app.
RUN python manage.py collectstatic --noinput -c
# Start app
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
