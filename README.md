Tily
===


Tily is a minimal URL shortener build with the Django web framework and MySQL.

---


Installation
------------

> **Note:**
> This installation guide assumes that python 2.7 and pip are installed.

First, install the dependencies.

```pip install -r requirements.txt```

Then, run the database migrations.

```$ python manage.py migrate```

> **Note:**
> The current database settings are expecting a **tily@localhost** user with the password **mypass** and all privileges on the databases **tily**  and **test_tily**. MySQL should be reachable at **localhost:3306** These settings can (and should) be changed in the file **tily/settings.py**.

Finally, run the tests to make sure everything works.

```$ python manage.py test```

Running the server
-----------------

```$ python manage.py runserver```

---

Checklist for production
------------------------

- Setup a proper way to serve static files. See: https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/
- Review Django settings. See: https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

Performance improvements
------------------------

- Cache redirection URLs.
- Get link analytics by analyzing server logs instead of storing values in the database.

---

Flow
----

1. The client displays a page containg a form for the user to input an URL to shorten.
2. When the user submits the form, the client POSTs the URL to the service through an AJAX request.
3. The server creates an entry in the database for the url if it doesn't already exist.
3. The server responds with a JSON object containing the shortened URL.
4. The client displays the shortened URL in the page.

Then, whenever the shortened URL is visited, it redirects the client to the original URL.

Endpoints
---------

- ```GET /``` serves the static file index.html.
- ```POST /``` creates a new short URL. It expects an ```url``` parameter which is the url to shorten. The output is a JSON document containing the shortened URL under the ```tiny_url``` key.
- ```GET /<tiny_url>``` outputs a permanent redirection (301) to the initial URL.

> **NOTE:** The URL shortening endpoint is at the root of the website in an effort to keep the URLs as small as possible.