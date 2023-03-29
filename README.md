Creating minimal working setup

1. Set up PostgreSQL via docker for local environment (docker-compose.yaml)
2. Then run docker-compose up -d to start a container
3. I use 5433 port to avoid potential conflict
4. In requirements.txt file I added packages: psycopg2-binary for working with Postgres and django-environ to retrieve Postgres
5. Whitenoise Package to serve static files for Django Admin
6. In settings.py file I load env variables
7. I set a default value for DATABASE_URL to allow running the Django project locally
8. Middleware is required to serve static files and specify the STATIC_ROOT variable
9. I added a unit tests check to the Django project. Tests use a Python standard library module unittest
10. To run SQS locally, we will use softwaremill/elasticmq-native Docker image.
11. Add the Celery package to requirements.txt and run pip install -r requirements.txt. 
12. Then, create a new file django_aws/celery.py
13. and add to the django_aws/settings.py 
14. tests.py helps us to run first tasks
15. I hit URL http://127.0.0.1:8000/create-task, the create_web_task view will add a new task to the local SQS
16. Start the local web server with python manage.py runserver, hit this URL several times, and look at the SQS admin page http://127.0.0.1:9325/.
17. I create a periodic task using Celery Beat.
18. Wait for several tasks in queue, stop the beat process and run the worker again celery -A django_aws worker --loglevel info. The worker will process beat_task tasks. 