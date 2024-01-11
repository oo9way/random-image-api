web: celery -A imagegenerator worker --loglevel=info & python manage.py migrate && gunicorn imagegenerator.wsgi  --bind 0.0.0.0:$PORT
