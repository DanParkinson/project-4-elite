# TESTING

A variety of exploratory tests were performed throughout the project.

## MANUAL TESTING

Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

## Super User

<details>
<summary>Click me</summary>

When i originally tried to login as a superuser i recieved this error.

![Error](docs/testing/1superuser01.png)

After using code institute support i had forgotten to add.

![CSFR](docs/testing/1superuser02.png)

Admin login now functions correctly.

![Admin Page](docs/testing/1superuser03.png)

</details>

## Creating Templates 

<details>
<summary>Click me</summary>

Create a top level directory to include your templates 

![Templates](docs/testing/2templates01.png)

connect the templates directory to *elite/settings.py*

![Templates](docs/testing/2templates02.png)

![Templates](docs/testing/2templates03.png)

Once the templates partials are populated. The server looks like this

![Templates](docs/testing/2templates04.png)

</details>

## Connecting CSS and JS

<details>
<summary>Click me</summary>

Connect the static directory to *elite/settings.py*.

![static](docs/testing/3static01.png)

Create you style.css as shown at the top level.

![static](docs/testing/3static02.png)

Edit base.html to load sytle sheet.

![static](docs/testing/3static04.png)

Connect script.js to base.html.

![static](docs/testing/3static03.png)

Server with backgorund colour and console message from javascrpit.

![static](docs/testing/3static05.png)

</details>

## AllAuth

<details>
<summary>Click me</summary>

- Install allauth using *pip3 install django-allauth~=0.57.0*
- Then add to requiremnts using *pip3 freeze --local > requirements.txt*

![AllAuth](docs/testing/4allauth01.png)

- Add AllAuth to installed apps.

![AllAuth](docs/testing/4allauth02.png)

- Add email confirmation set to none so no errors are thrown.

![AllAuth](docs/testing/4allauth03.png)

- Add AllAuth to middleware

![AllAuth](docs/testing/4allauth04.png)

- Add site handling.

![AllAuth](docs/testing/4allauth05.png)

- Use terminal command shown below to find allauth template files

![AllAuth](docs/testing/4allauth06.png)

- Use this command to add them to the directory.

![AllAuth](docs/testing/4allauth07.png)

- Templates in directory

![AllAuth](docs/testing/4allauth08.png)

- Set debug to False and redlopy on Heroku. Styles now show on AllAuth templates.

![AllAuth](docs/testing/4allauth09.png)

</details>

## Authentication 

<details>
<summary>Click me</summary>

- Users can create accounts using django allauth and views change.

![Authentication](docs/testing/5authentication01.png)

- Users can log out and views change

![Authentication](docs/testing/5authentication02.png)

- The database stores the user correctly. 

![Authentication](docs/testing/5authentication03.png)

</details>

## Account editing

<details>
<summary>Click me</summary>

Tests were performed to check that:
- User name and email are updated in the database
- User password change was used to relogin 
- Deleting accounts removes the user from the database

</details>
