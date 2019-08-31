# World of Fitness

Application allow user to discover world of fitness main type of exercise he can practice in the gym or home, each exercise show to the user with comprehensive explanation and good quality picture how to practice exercise safely to maximum efficiency.The main business model of the app is very simple - user can browse exercise catalogue for free but if they really want to best result they can purchase fitness program, tailor made for them base only on user physical data and current fitness level. 
[Fitness-world](https://fitness-world.herokuapp.com/)

## UX
 
User Stories
* As visitor I want to have simple welcome page explain why the project exist.
* As visitor I want to have easy to find link to functional page of the application.
* As visitor I want to have easy to find log in or register links on the welcome page.
* As visitor I want to have nice overview all exercises page with very brief description on each exercise.
* As visitor I want to able when click on exercise to able to see full description of the exercise with full screen picture.
* As visitor I want when I decide to be able to use main future of the app and buy  fitness program and easy to find the link to do it.
* As visitor I want to have hassle-free purchase so I expect app not to collect sensitive personal information as DOB etc. and use secure payment provider and not to store my credit card details. 
* As visitor I want when successfully paid and input my details app to show me generate fitness program immediately.
* As visitor I want to be able to search for exercise at any time.  
* As visitor I want to have option to log out from my account at any time.
* As visitor I want to be able to log in in my account and use my own profile page where I can see my details and any fitness program I purchased.


## Features

1. The home page welcomes the visitor, gives a visitor quick overview of the story behind the application and what it is purpose. 

2. On the home page I user able to click on log in link( if already have account) or register link for new user. 

3. After successfully log in/ register user is redirect to exercises page where he/she can see all exercises and search bar on top right corner under navigation bar. 

4. In navigation bar user can see link to log out from the page which it'll take user back to welcome page and buy fitness program link which will redirect user to from where he/she can input details required from the app to generate tailor made fitness program.

5. if user click on any exercise on exercises page on View more.. button in exercise container user is redirect to page where exercise picture is show on full screen and description how to perform exercise is located under picture.

6. if user decide to purchase program he is redirect to your detail page where form with four field first require user height in centimeters , second require user weight in kilos and third require user age , fourth field is user to choose current fitness level where 3 choices could be found: Beginner, Medium, Advance, if user try to submit the form with empty field form will show error message.

7. if your details form is successfully fill and submit user will ve redirect to payment page where on the top on the page he/she can find how much will be charged for fitness program and payment form require credit/debit card details. if user try to submit the form with empty field form will show error message.

8. if user paid successfully app redirect user to new page where his/her fitness program appear as table.

9. Every time user is log in he can go to profile page where he can see his email used for registration and his details and purchased fitness program if user not have any message will show advice user to purchase fitness program.  



## Technologies Used

As this project was build application for Full stack Development Milestone project , [Django](https://www.djangoproject.com/) was used as main framework.
all the back end logic that makes this project work was written in Python 3.6.

Other technologies used in this project are:

- HTML, the most basic building block of the Web for writing the basic front-end content.

- CSS, a stylesheet language for styling the page.

- [Javascript](https://www.javascript.com/) used to written logic  front end of the application.

- [JQuery](https://jquery.com/) for allowing the Javascript functionality in Bootstrap and my custom script to work.

- Python 3.6 for back end logic of the application

- [Bootstrap](https://getbootstrap.com/), a front-end framework for general responsiveness. For components used such as the navbar with burger icon which makes the app easy to use on mobile.

- [Postgres](https://www.postgresql.org/) for database storage and query writing.

- [Stripe](https://stripe.com/docs/stripe-js) to process customer payment without app store customer card details.

- [Travis CI](https://travis-ci.com/) was used for continuous integration for build and test software project.


## Testing

Custom automated testing has been done on this project. for continuous integration and testing is used [Travis CI](https://travis-ci.com/). All test could be found in file start with test_... .py  each app is checked for models input validation, views validation, valid html, accounts app is also check for valid user.

For the user stories, the manual testing process is as follows:

- welcome page/home page will have under welcome text have button with text "To start your journey just press here to register" which when press it must redirect user to register  page of the application where user can see the register when fill his details in the form if he left any field empty and try to submit the form empty form field will show him error and if user try to register with someone else email or already register field will show me message email must be unique.


 - After successfully register/login user is redirect to exercises page where he is able to see all exercise as little block where name on the exercise and picture appear and also button says View more.
    
 - When user choose view more button should be redirect to single exercise page where he can see enlarge picture of the exercise and description under picture.


- if user press buy fitness program link on the navbar should be redirect to your details page where he able to see details form if details form is successfully filled in when press submit user should be redirect to payment page if any field left empty error message should appear on the screen show user which field must fill before submit the form.

- if user try to submit any form in the app with empty field django error message should appear show what type of data expect and field which must be fill.
  
 - if user successfully submit details form should be redirect to payment page where on top of the page under navbar should show price for the program and under that payment form asking customer for card details.
 
 - Because purpose of the project is to demonstrate ability to use django all stripe API are still in test key mode and won't cause real charge on card details but for test purpose card number could be 4242424242424242 for VISA ans CVV = 100 any month and year in the future will do the job for expire date and if all this is input in the form and press submit user should be redirect to th fitness program page where user can see his 12 weeks program in easy to read table 
 
     
- if user press log out he should be redirect to home/welcome page

- if user is log in and press profile link should be redirect to his profile page where he can see his details and fitness program he purchase if user didn't purchase any fitness program yet all he able to see on profile page is his username and email use for registration and message saying: "you don't purchase any fitness program yet but you can do it here!" and link button to purchase program.

- User can reset choose password at any time by clicking reset password under login page any field in reset password should not be left empty or django message will appear say user error type and show which field must be fill.

- In the top left corner application contain search bar where user can type name of couple letters of exercise and exercises with relate name should appear on the screen.
  

## Deployment and Security

Development version on the application are develop on
the local editor for whole project [AWS Cloud9](https://aws.amazon.com/console/).


All secret keys is store in temporary file in editor for development stage of the project which is include in .gitignore and that way is prevent to be publish in public accessible places, for production stage all secret keys are clone directly to [Heroku](https://www.heroku.com/)

Deployment:
Production version of the project is deployed to [Heroku](https://fitness-world.herokuapp.com/)

GIT Repository [here](https://github.com/rokambol/World-of-Fintess) clone repository and run it to to your own editor. 

1. in your own editor in bash terminal/ pip/script terminal use following command:
sudo pip3 install django 1.11 (correct version for this project).

and then:

sudo pip3 install requirements.txt

- that will install all neccessery package to can run the project.

2. you need to gain new Stripe API key from  [Stripe](https://stripe.com/docs/stripe-js)
to be able to proceed the payment on the page.

3. All static file is stored in cloud service as [AWS buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) so project have only basic bootstrap style.

4. you need to replace all secret keys instances with your own in settings.py 

5. Create new DB instance so you data store outside the project (cloud service as AWS is prefere)

6. replace DATABASE keys in your setting.py 

7. After Database is successfully created and connect to your project run following command:

-  python3 manage.py makemigrations
-  python3 manage.py migrate 

- that command should transfer models in your db tables

run following command if everything is successful:

python3 manage.py createsuperuser

- after this command in terminal will ask you for username, e-mail and password and repeat password after successfully created that you can you admin page after running project from terminal.

- you should be able to edit and create new exercise from your admin page.

Have fun!

## Credits
I would like to thank my fellow students for their encouragement, tips and bug reporting along the way. 

Many thanks to my mentor Guido Cecilio Garcia Bernal  for his help and tips.

### Content

The photo of marker used in this site was obtained from [google.com](https://google.com/).
