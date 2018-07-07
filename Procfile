web: gunicorn config.wsgi:application
worker: celery worker --app=teachers_toolkit.taskapp --loglevel=info
