# Exotics Ecosse
Exotics Ecosse is a high end car rental company where you can hire SUV's, Luxury cars, and Supercars for days, weeks, or months.
While catering to the real car enthusiast who can experience the thrill of driving some of the fastest and most powerfull cars in the world.
It's also for the businessman who wants to impress a client, or for people attending a special event like a wedding or an anniversary,
or simply to treat themselves.
There is also the instagram generation market, where people want to upload pictures of themselves surrounded by expensive trinketry to
show the world that they are leading their 'best life'!
Exotic cars are expensive to buy, keep, and run, so Exotics Ecosse has the facility for owners of such to make their vehicles available
for hire to help with these ownership costs.
They can register as a vehicle owner to become a super user, and this gives them access to add, edit, and delete their vehicle 
from the site if and when they choose.

## UX
Users of Exotics Ecosse will find a simple to use, intuative layout with clearly defined task buttons to take them directly to the 
category of vehicles they are interested in. Alternativley there is a search facility to look for a specific vehicle or they can
select to browse all of the categories of available vehicles. Once into the vehicle category it's then a quick and easy process
to select a vehicle and get through to the cart and checkout area's. Users who register for an account will have access to their
own profile page which allows them to save their details which will make future bookings even faster, and also allow them to
see their previous bookings in their order history.

## User goals

### As a rental customer:
* I want to view all vehicles
* I want to view seperate categories of vehicles
* I want to search for a named vehicle
* I want to sort vehicles by price
* I want to sort vehicles by rating
* I want to see vehicle details
* I want to see cart updated when a vehicle is added 
* I want to be able to remove a vehicle from cart
* I want to be able to amend number of rental days
* I want an online payment facility
* I want a confirmation email 

### As a registered rental customer:(As above but to also include)
* I want to save my personal details to expedite future bookings
* I want to view my previous bookings

### As a vehicle owner:
* I want the ability to add a vehicle including images, description, and price.
* I want the ability to edit and delete my vehicles

## Wireframes 
Wireframes for this project were completed on balsamiq and are available to view under seperate file in the repository.

## Features

* Navbar & Header are clean and simple in design for ease of use immediately by the user.
* An information banner also acts as a home button relevant on mobile.
* The hompage is minimal with a simple statement, a button, and a striking hero image.
* The category pages are of a matching layout with image, name, price, and rating for each of the vehicles.
* Vehicle detail page includes a larger image, details, description, number of days selector, continue shopping and an add to cart button.
* Selecting add to cart opens a toast confirming your selections and inviting you to proceed to checkout.
* In cart page you can amend or remove vehicle or proceed to checkout.
* Checkout page consits of a form for user details & card details on left and booking summary on right.
* Register for an account takes user details but not card info.
* Thank you page has a form which lists all transaction details on left and a success toast opens on right.
* Vehicle management page for owners only allows submission of vehicle details and gives access to edit and delete.

## Features to implement in future
* Functionality for owners to specify available dates 
* A Merchandise store for Exotics Ecosse brand. Shirts, t-shirts, hats, keyrings, flasks etc
* Option to select the size of a vehicle by number of seats
* Fix widgets.py, some checkout.py, and some profiles.py files. Attempts to adjust line lengths breaks code, needs further investigation.

## Technologies Used
* HTML the standard markup language
* CSS to style html
* PYTHON high level programming language
* JAVASCRIPT to enable creation of dynamically updating content
* JQUERY to simplify DOM manipulation
* BOTO3 to edit AWS resources from Python scripts
* JINJA to generate any markup and source code
* PILLOW for processing image files
* GOOGLE FONTS for text
* FONT AWESOME for icons
* GUNICORN to run Python web application
* BOOTSTRAP for responsive design
* DJANGO the Python Web framework
* GIT to manage version control
* GITHUB to share and store code
* GITPOD as my Integrated Development Environment
* SQLITE3 as development database 
* AWS S3  for static and media files 
* STRIPE  for payment management
* HEROKU  for deployment
* POSTGRESQL for production
* BALSAMIQ for Wireframes

## Testing
I have run testing on
* Chrome developer tools
* W3C Validator for HTML
* W3C Validator for CSS
* JSHint for javascript 
* Pep8 for Python

It has been tested on
* Google Chrome
* Firefox
* Safari

It has been checked on these screen sizes and renders well on all
* Desktop
* Laptop
* Ipad
* Iphone

I used the W3C Validator which through up various errors which I believe were caused
by the validator having problems with Django's template code.

## Deployment
This site was created using GITPOD, stored in GITHUB, and deployed through HEROKU.

The deployed link for the site is: https://pt70-exotics-ecosse.herokuapp.com/

To make a payment when testing this app, please use the following details:

* Card number: 4242 4242 4242 4242
* CVC: any 3 numbers
* Date: any date
* ZIP Code: any 5 numbers

You can clone this project from this repository by,

Clicking on the "clone or download" button at the top right Copy the URL Change the current working directory
to the location of your clone directory Enter git clone and paste in the URL:

## Credits

### Content
I received inspiration for this project from the final module in the code institute full stack developer course.
It was an invaluable resource and guide, and as such used it as my template, referring to the video tutorials throughout. 

### Media
The photos used in this site were obtained from Google Images.

### Acknowledgements
The colour scheme for this project was inspired by the TV advertisement for 'G-Tech' products, which I think has a clean sharp look.

