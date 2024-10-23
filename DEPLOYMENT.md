# DEPLOYMENT

This is where my deployment process will be documented.

## Install Django and packages, Create Django Project, Run Server and allow hosts

<details>
<summary>Click me</summary>

- Install django with *pip3 install django~=4.2.1*
- Install gunicorn with *pip3 install gunicorn ~=20.1*
- Install whitenoise with *pip3 install whitenoise~=6.5.0*
- Install psycopg2 and dj_database_url with *pip3 install dj_database_url~=0.5 psycopg2~=2.9*

- Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it.

![requirements.txt after install](docs/local_deployment/01-requirements.txt.png)

## Create Django Project 

- Using the command *django-admin startproject elite .* creates our django project at the top level.

![Django Project Directory](docs/local_deployment/02-django-project.png)

## running the server and allowing hosts

Using the command *python3 manage.py runserver* opens the server in port 8000. The server needs allowed hosts in elite-cuisine/settings.py to be added.

![Disallowed host](docs/local_deployment/03-disallowed-host.png)

![Successful project](docs/local_deployment/04-install-succesful.png)

</details>

## Heroku Deployment

<details>
<summary>Click me</summary>

Navigate to your Heroku dashboard and create a new Heroku app.

![Start app](docs/heroku_deployment/01-start-app.png)

![Create app](docs/heroku_deployment/02-create-app.png)

Add DISABLE_COLLECTSTATIC with a Value of 1 to stop Heroku uploading static files.

![DISABLE_COLLECTSTATIC](docs/heroku_deployment/03-collectstatic.png)

Create a Procfile to allow Heroku to deploy using Gunicorn.

![Procfile](docs/heroku_deployment/04-procfile.png)

Add Heroku to allowed hosts in elite_cuisine/settings.py.

![Heroku host](docs/heroku_deployment/05-heroku-host.png)