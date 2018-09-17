#!/bin/bash

#!/usr/bin/env bash
set -e

cmd="$@"

arrData=(${DATABASE_URL//:/ })

hostData=(${arrData[2]//@/ })
hostData=${hostData[1]}
portData=(${arrData[3]//// })
portData=${portData[0]}

while ! pg_isready -h "${hostData}" -p "${portData}" > /dev/null 2> /dev/null; do
   sleep 1
 done

echo Apply database migrations.
python manage.py migrate --noinput

echo Collect static files
python manage.py collectstatic --noinput

echo Creating admin user
python manage.py initadmin

echo Starting Gunicorn.
exec gunicorn movie_trailer_website.wsgi:application \
    --name app \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=debug \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/access.log \
    "$@"