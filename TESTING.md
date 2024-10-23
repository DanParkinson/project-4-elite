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
