create env

activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

celery -A my_project worker -l info

celery -A my_project beat -l info

flower -A my_project --port=5555
