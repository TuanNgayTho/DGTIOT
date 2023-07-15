pip install -r requirements.txt
celery -A Led_project beat -l INFO
celery -A Led_project worker --pool=solo -l info
daphne Led_project.asgi:application
daphne -p 8001 Led_project.asgi:application
daphne -b 103.184.113.154 -p 8001 Led_project.asgi:application
Python .\manage.py runserver
