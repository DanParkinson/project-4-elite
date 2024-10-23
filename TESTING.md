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
