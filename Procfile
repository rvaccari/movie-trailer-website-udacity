release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput
release: python manage.py initadmin
web: gunicorn movie_trailer_website.wsgi --log-file -
