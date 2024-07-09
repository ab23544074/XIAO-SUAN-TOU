release: python manage.py migrate
web: gunicorn myweb.wsgi:application --log-file - --log-level debug

