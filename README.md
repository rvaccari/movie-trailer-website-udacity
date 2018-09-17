# A movie trailer website in Django
This is the source code for a Movie Trailer webpage. It displays a list of movie trailers picked personally by Rodrigo Vaccari. You can see a little description of the movie when you just hover over the movie image.

# Steps
How to install in locally (supposing you have git and python >= 3.6 installed):

```console
git clone https://github.com/rvaccari/movie_trailer_website.git
cd movie_trailer_website
cp contrib/env-sample .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py initadmin
python manage.py runserver
```

If you want run your amb using docker, run:
```
docker-compose up -d
```

# License Details

The AGPL license here cover everything relate to source code but Python Pro logo and Image.
So you need to change this data for you own trademark.


Have fun!
