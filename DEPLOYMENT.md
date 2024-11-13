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

Connect Heroku to your Github account.

![Connect Github](docs/heroku_deployment/06-connect-github.png)

Click deploy branch and wait for completion.

![deploy](docs/heroku_deployment/07-deploy.png)

Add Eco Dynos.

![Eco Dynos](docs/heroku_deployment/08-eco-dynos.png)

</details>

# PostgreSQL database 

<details>
<summary>Click me</summary>

Create an env.py file in the top directory and use this code. The postgreSQL code was generated from Code Institute. It has been redacted from the image.

![env.py](docs/heroku_deployment/09-env.png)

Use the following code to connect the env.py in the elite_cuisine/settings.py.

![connecting settings.py to env.py](docs/heroku_deployment/10-settings-env.png)

In the elite_cuisine/settings.py file, disconnect the splite database by commenting out the code.

![disable sqlite](docs/heroku_deployment/11-sqlite.png)

Use dj-databse-url to connect.

![dj_database](docs/heroku_deployment/12-database.png)

</details>

## Create super user

<details>
<summary>Click me</summary>

- Using the terminal command *python3 manage.py migrate*, create a database.
- Create a superuser using djangos built in admin and auth apps using temrinal command python3 manage.py createsuperuser.

</details>

## Connect Heroku to the postgreSQL

<details>
<summary>Click me</summary>

- Deploy a new branch in Heroku.

- Create a new convig-var using the name DATABASE-URL and a value of your postgreSQL. This connects Heroku to the postgreSQL.

![ConfigVar](docs/heroku_deployment/13-heroku-postgresql.png)

</details>

## Secret Key 

<details>
<summary>Click me</summary>

Generate a secret key using letters, numbers and symbols that is hard to guess. This is used to keep information private. Add it to the env.py file with the following code.

![env secret key](docs/heroku_deployment/14-secret-key.png)

Update the settings.py file.

![Settings secret key](docs/heroku_deployment/15-secret-key-settings.png)

Add secret key as a config-var to Heroku. The name should be SECRET_KEY. The value should be your secret key value.
If done correctly, both local and Heroku deployment should work.

</details>

## Deploy Static Files

<details>
<summary>Click me</summary>

Add white noise to middleware. Make sure it is the same location as the photo.

![Whitenoise](docs/heroku_deployment/16-whitenoise.png)

add a static root to elite/settings.py

![Static root](docs/heroku_deployment/17-staticpath.png)

collect static in the terminal.

![Collect static](docs/heroku_deployment/18-collectstatic.png)

create a runtime.txt file with your version of python IDE. you can get this through the terminal command *python -v*

![runtime.txt](docs/heroku_deployment/19-runtime.png)

set debug to False.

![Debug](docs/heroku_deployment/20-debug.png)

remove the configvar in Heroku of DISABLE_COLLECTSTATIC.

![ConfigVar](docs/heroku_deployment/21-disablecollectstatic.png)

Deploy the site and static files should now load.

![deploy Heroku](docs/heroku_deployment/22-deployedsite.png)

set debug back to True.

![Debug True](docs/heroku_deployment/23-debugtrue.png)

</details>