# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

EXPOSE 8000

# Create /app directory
RUN mkdir -p /app
WORKDIR /app

# Install  requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app.
COPY . /app/

# Collect all static files in app.
RUN python manage.py collectstatic --noinput

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
