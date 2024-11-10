# TESTING

A variety of exploratory tests were performed throughout the project.

## MANUAL TESTING During DEVELOPMENT

Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

### Super User

<details>
<summary>Click me</summary>

When i originally tried to login as a superuser i recieved this error.

![Error](docs/testing/1superuser01.png)

After using code institute support i had forgotten to add.

![CSFR](docs/testing/1superuser02.png)

Admin login now functions correctly.

![Admin Page](docs/testing/1superuser03.png)

</details>

### Creating Templates 

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

### Connecting CSS and JS

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

### AllAuth

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

### Authentication 

<details>
<summary>Click me</summary>

- Users can create accounts using django allauth and views change.

![Authentication](docs/testing/5authentication01.png)

- Users can log out and views change

![Authentication](docs/testing/5authentication02.png)

- The database stores the user correctly. 

![Authentication](docs/testing/5authentication03.png)

</details>

### Account editing

<details>
<summary>Click me</summary>

Tests were performed to check that:
- User name and email are updated in the database
- User password change was used to relogin 
- Deleting accounts removes the user from the database

</details>

### Making reservations

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

### homepage next reservation 

<details>
<summary>Click me</summary>

- The home page now shows the next reservation 

![hompage next reservation ](docs/testing/7next_reservation01.png)

</details>

### Double Booking 

<details>
<summary>Click me</summary>

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

### Users can see availble times on the day that they book if table in unavailable at their chosen time

- users can now see available times when inputting a reservation that is taken

![Double booking](docs/testing/8double_booking06.png)

- Users are now told that there are no available times if fully booked 

![Double booking](docs/testing/8double_booking07.png)

- Users booking a reservation today no longer see expired times in available times. current time of picture is 10:27

![Double booking](docs/testing/8double_booking08.png)

</details>

### my reservations page 

<details>
<summary>Click me</summary>

- users can see all of their reservations that are in the future

![my reservations](docs/testing/9my_reservations01.png)

- Users can now edit their reservations 
- form prepopulates reservation details when editing except for time

![my reservations](docs/testing/9my_reservations02.png)

- reservation details can be chnaged
- my reservations updated

![my reservations](docs/testing/9my_reservations03.png)

- users can now delete reservations 

![my reservations](docs/testing/9my_reservations04.png)

- my reserations updated

![my reservations](docs/testing/9my_reservations05.png)

- database deletes and changes the reservations

![my reservations](docs/testing/9my_reservations06.png)

</details>

### staff reservation overview

<details>
<summary>Click me</summary>

- Only staff can see all reservations for a selected day

![reservation overview](docs/testing/10reservation_overview01.png)

![reservation overview](docs/testing/10reservation_overview02.png)

</details>

### Double booking with multiple tables

<details>
<summary>Click me</summary>

There are 8 tables in the restaraunt each with a maximum seating capacity. Tables need to be linked with reservations they can accomodate and ensure that the booking has at least 1 hour to enjoy their reservation. 

For reference 
- table 1 2 guests
- table 2 2 guests 
- table 3 4 guests 
- table 4 4 guests 
- table 5 6 guests 
- table 6 6 guests 
- table 7 8 guests 
- table 8 8 guests 

- both table 1 and 2 can only hold 2 people. Currently they are booked. 

![11tables01](docs/testing/11tables01.png)

- If a user trys to book with 1 or 2 guests a bigger table capacity will be used.

![11tables02](docs/testing/11tables02.png)

- If a user books a reservation with 2 guests an hour after a 2 capacity finishes they get assigned the samllest table.

![11tables03](docs/testing/11tables03.png)

- If a user trys to book a capacity of 8 people tables 7 and 8 will be used.

![11tables04](docs/testing/11tables04.png)

- If a user trys to book an 8 capacity table when table 7 and 8 are booked they will be given availble times based on their capacity. This proves multiple tests:

- table 7 and 8s bookings are currently staggered. The 11:15 available time is okay for 1 table and not the other so only 1 booking can be made at this time.
- tables 5 and 6 are free which have a capacity of 6 guests. Their available times are not shown as they cannot be seated. 
- There are plenty of times for the day still available but i have sliced them down to the nearest times 3 either side.
- these time are available on other days so the date is checked correctly
- Since there are two tables that can hold this capacity there will be duplicated available time slots e.g. 11:00, 11:00. Only one is shown to not confuse users. 

- ![11tables05](docs/testing/11tables05.png)

</details>

## AUTOMATED TESTING 

Since the site is relativly small manual testing can cover the testing required. If the site is too grow further I will implement automated testing to ensure all code is checked.

## VALIDATORS 

[W3C Markup Validator](https://validator.w3.org/)

### Not SIGNED IN 

<details>
<summary>Click me</summary>

#### home page

- error with header not being in body tag. extra divs removed.

![Not signed in html errors](docs/testing/12htmlvalidator01.png)

![Not signed in html errors](docs/testing/12htmlvalidator02.png)

#### About us 

- no errors 

![Not signed in html errors](docs/testing/12htmlvalidator03.png)

#### menu page 

- no errors

![Not signed in html errors](docs/testing/12htmlvalidator04.png)

#### sign up page 

- no errors 

![Not signed in html errors](docs/testing/12htmlvalidator05.png)

#### Login page 

- missing closing div on form element 

![Not signed in html errors](docs/testing/12htmlvalidator06.png)

![Not signed in html errors](docs/testing/12htmlvalidator07.png)

</details>

### Signed in 

<details>
<summary>Click me</summary>

#### home page 

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator08.png)

#### make reservation

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator09.png)

#### edit reservation 

- stray closing div tage removed 

![Signed in html errors](docs/testing/12htmlvalidator19.png)

![Signed in html errors](docs/testing/12htmlvalidator020.png)

#### delete reservation 

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator021.png)

#### my reservations 

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator10.png)


#### my account 

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator11.png)

#### edit account details 

- no errors 

![Signed in html errors](docs/testing/12htmlvalidator12.png)

#### change password 

- buttons with links changed to anchors 

![Signed in html errors](docs/testing/12htmlvalidator13.png)

![Signed in html errors](docs/testing/12htmlvalidator14.png)

#### delete account 

![Signed in html errors](docs/testing/12htmlvalidator15.png)

#### reservation overview 

- closed container div

![Signed in html errors](docs/testing/12htmlvalidator16.png)

![Signed in html errors](docs/testing/12htmlvalidator17.png)

#### log out 

![Signed in html errors](docs/testing/12htmlvalidator18.png)

</details>

### CSS VALIDATION

[Jigsaw](https://jigsaw.w3.org/css-validator/)

<details>
<summary>Click me</summary>

- 1 error found with incorrect input. removed it as it contributes nothing

![CSS errors](docs/testing/13cssvalidator01.png)

![CSS errors](docs/testing/13cssvalidator02.png)

</details>

### JS VALIDATION 

[JSHint](https://jshint.com/)

<details>
<summary>Click me</summary>

no custom js was used to no validation needed

</details>

### PYTHON VALIDATION 

[PEP8](https://www.pythonchecker.com/)

<details>
<summary>Click me</summary>

- no errors found in any python 

- home views

![Python errors](docs/testing/14pythonvalidator01.png)

- profiles views

![Python errors](docs/testing/14pythonvalidator02.png)

- reservation forms

![Python errors](docs/testing/14pythonvalidator03.png)

- reservation models 

![Python errors](docs/testing/14pythonvalidator04.png)

- reservation views 

![Python errors](docs/testing/14pythonvalidator05.png)

</details>

## Lighthouse 

<details>
<summary>Click me</summary>

- All light house checks passed 

![Lighthouse checks](docs/testing/15LH01.png)

![Lighthouse checks](docs/testing/15LH02.png)

![Lighthouse checks](docs/testing/15LH03.png)

![Lighthouse checks](docs/testing/15LH04.png)

![Lighthouse checks](docs/testing/15LH05.png)

![Lighthouse checks](docs/testing/15LH06.png)

![Lighthouse checks](docs/testing/15LH07.png)

![Lighthouse checks](docs/testing/15LH08.png)

![Lighthouse checks](docs/testing/15LH09.png)

![Lighthouse checks](docs/testing/15LH10.png)

![Lighthouse checks](docs/testing/15LH11.png)

![Lighthouse checks](docs/testing/15LH12.png)

![Lighthouse checks](docs/testing/15LH13.png)

![Lighthouse checks](docs/testing/15LH14.png)

</details>

## Browser checks 

- webiste has been checked on chrome, firefox, bing

## Unresolved issues 

- the edit reservations page prepopulates all fields except for the time field 

- During my html validation. The change password page flagged on google chrome as a dangerous site. This did not happen on any other browser. 

- Users cannot request an email to change their passwords.

- users are not sent email confirmation of their reservations or account details changing