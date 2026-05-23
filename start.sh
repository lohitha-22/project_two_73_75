
#!/bin/bash 
python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn jango_deployee.wsgi:application --bind 0.0.0.0:$PORT