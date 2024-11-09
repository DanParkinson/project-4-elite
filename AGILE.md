# AGILE

This is where I will document my agile approach. It will be set into phases to help me organise my work. After a few false starts where i found myself getting lost, this will help me document my thoughts. Because of the false starts my README.md has already been created. 

## Phase 1

<details>
<summary>Click me</summary>

- Setup repo.
- Create Django project.
- Install basic dependencies and add to requirements.
- Create procfile to deploy to Heroku.
- Create app on Heroku.
- Link GitHub repo to Heroku app.
- Test to deploy working project ASAP.
- Document project creation and deployment.
- Perform design thinking exercise for features to include in project.
- Add user stories to readme.
- Add wireframes to readme.
- Mock up initial database design and document in readme.
- List and link technologies used in readme. ------------------------------
- Use GitHub projects. Create user stories.

</details>

## Phase 2

With everything set up I am going to style the homepage a litte with bootstrap to allow me to navigate around the website as needed.

With basic stylings in place i can now navigate around the website. I can make any adjustments as nessercary when i am working on other parts.

## Phase 3 

Before creating my reservation model I need users to create accounts. I am going to use Django AllAuth for this.

Users need to be able to:
- create accounts 
- login/ log out
- view account details
- edit account details
- delete account

- navigation bar and homepage buttons should change if user is authenticated.

User Stories:

1, 3, 5, 6, 7

- Now I need users to be able to view their account details, be able to edit them, and delete their account.

User Stories:

8, 9, 10

## Phase 4 

### make_reservations

Now that users can login. Users need to be able to make reservations. 

- User can access a form to submit a reservation --
- Reservation is linked to user --
- User can view their nearest reservation on the homepage --
- User can view all of the reservations in my reservations in order --
- User can edit their reservation
- User can delete their reservation 
- User cannot double book a reservation. --
- Reservation form shows available reservations. -- 

Now that users can book a reservation. I want users to not be able to double book. I will start with 1 table in my restaraunt and each table needs to be held for one hour. So the reservation needs to check for reservations before and after their chosen booking time to see if it is available. I will use timedelta for this. 

Now that this works. I need users to be able to see the available booking times for that day so that booking is easier.

So many issuses with this. It is the end of my session but a lot of problems need to be addressed:

- users can now see available time options if reservation is already taken
- i got caught up in creating the logic that i forgot to make new functions for each part. These need rewriting to improve readability as i was getting VERY confused when trying to get the logic to work. I now have one massive function which is not acceptable.

### my_reservations

If users have multiple reservations it would be good to be able to see all of the reservations. Once users can see their reservations they need to be able to edit and delete these reservations. 

- my_reservations shows all of the users reservations
- needs to filter out expired reservations 
- styled

### Editing reservations 

A new view needs to be created that allows users to edit their reservation. This should:
- pull the users reservations from the database
- prepopulate the form with the information
- check that the new reservation is available
- users should only be able to edit their own reservations
- CRUD needs to be used because most of the logic is similar to make_reservations.

### Deleting a reservation 

Users need to be able to delete a reservation if needed

## Phase 5

Now that users can fully control their own reservations. Admins need to be able to view all reservations on any given day.
Phase 5 was mostly about tidying up the website design and fixing any issues that i noticed. Now that the site is functioning I can move onto phase 6.


## Phase 6 
During phase 6 multiple tables were implemented. The first attempt of this was poor and I realised that the whole structure of make_reservations needed remaking. Now the website can implement as many tables as it needs. edit_reservations was simple as i could just copy the code over from make_reservations.

I have decided to make sure that tables have a capacity assigned to them and that reservations are only accepted if the capacity can hold the table. this SHOULD be a simple change in logic for how the seat is assigned. the hard part will be to make sure that a reservation of two people take up the smallest table possible. This was simpler than I thought. 

## Phase 7 
Now to do some automated testing. I also need to update the manual testing in TESTING.md


# fixes
- password request change
- location




