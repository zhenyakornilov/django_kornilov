web: gunicorn django_kornilov.wsgi --log-file -
celery: celery worker -A django_kornilov -l INFO -concurrency 4 -P solo
celery: celery -A django_kornilov beat -l INFO