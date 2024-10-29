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

## Making reservations

<details>
<summary>Click me</summary>

Multiple checks were made for making reservations

- phone number has to be positive number

![make reservations checks ](docs/testing/6make_reservations02.png)

- number of guests has to be between 1 and 9 

![make reservations checks ](docs/testing/6make_reservations03.png)

- reservation date has to be today onwards

![make reservations checks ](docs/testing/6make_reservations04.png)

- time fields are 15 minute intervals

![make reservations checks ](docs/testing/6make_reservations05.png)

- reservations are saved to the databse

![make reservations checks ](docs/testing/6make_reservations01.png)

- Users recieve error message when a datetime is selected that is in the past 

![make reservations checks ](docs/testing/6make_reservations06.png)

</details>

## homepage next reservation 

- The home page now shows the next reservation 

![hompage next reservation ](docs/testing/7next_reservation01.png)

## Double Booking 

### With 1 table 

Users can no longer book reservations that are two hours behind or ahead of an already existing reservation

- booked reservation

![Double booking](docs/testing/8double_booking01.png)

- Attempt to book 1 hour 45 mins after 

![Double booking](docs/testing/8double_booking02.png)

- attempt to book 1 hour 45 minutes before

![Double booking](docs/testing/8double_booking03.png)

- attempt to book 2 hours either side succesful

![Double booking](docs/testing/8double_booking05.png)

- attempt to book on another day but same time

![Double booking](docs/testing/8double_booking04.png)

## Users can see availble times on the day that they book if table in unavailable at their chosen time

- users can now see available times when inputting a reservation that is taken

![Double booking](docs/testing/8double_booking06.png)

- Users are now told that there are no available times if fully booked 

![Double booking](docs/testing/8double_booking07.png)

- Users booking a reservation today no longer see expired times in available times. current time of picture is 10:27

![Double booking](docs/testing/8double_booking08.png)