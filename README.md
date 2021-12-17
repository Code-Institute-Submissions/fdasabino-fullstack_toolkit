# STHLM-foodies - Fresh food delivery

<img src="https://res.cloudinary.com/frank2021/image/upload/v1639559966/STHLM-foodies/frame-sthlm_vxctvo.png">

## Project Goals

This page was designed with the intent to create a e-commerce website that allows B2C interactivity.
Showing the skills required in order to fullfil the requirements of the project milestone number 4 of the Code Institute and it's learning outcomes.

## Deployed Application

You can access the application [here](https://sthlm-foodies.herokuapp.com/).
Please create an account by clicking on the login or register link on the top right corner. You'll need an account to be able to use the application's full functionality.

## UX

This application was developed to host a multi-product store, that can accommodate a variety of products.
In the section below you will find our user stories and some more information about the user experience and how users can interact with this website.

## User Stories

### Visitors can:

- Browse products by categories.
- Add, Update and Remove items from their basket.
- Create a customer account, allowing users to have full control over their account performing CRUD functionality.
- Add, Update and Remove alternative delivery addresses.
- View order history, with a full breakdown of the items ordered.
- Create and pay for order with ease, and without any additional steps, making it easy to place orders on the go.
- Pay for products, using paypal or credit card.

### Site owners can:

- Add new products and have them automatically display on the website.
- Edit product details, for example, price description, pictures etc.
- View the status of all customer orders, so that I can efficiently manage the orders.
- Check for customer data provided by paypal, and make sure payments went through before the order is sent.
- Have full control over customer details, for example, addresses, accounts linked, and products ordered.

## Features

### Existing Features

This application was divided in 5 main components, that are connected, and are responsible for a different set of
features. These are connected with the django messaging framework and produce feedback to the user.

#### Core

Core is the main component, it holds all main functionality involving the application in settings.py and urls.py.

#### Account

This application is responsible for all account related features, login, logout, account creation and deletion,
password changes and so on.
I have utilized some templates provided by django allauth, but have overridden the main auth functionality by creating a custom account manager class based on the django-allauth model.

#### Basket

The basket application handles all the basket related features such as add, update and remove items. This feature was built using the browser session to hold product data. This application works hand in hand with the checkout and order application.

#### Checkout

The checkout application handles all the checkout related features including delivery method selection, address
selection and payment.

#### Order

The order application handles all the order related features, essentially adding and storing the orders on the database.

#### Store

The store application handles all the store related features, being responsible for storing all the product data.
I have implemented this database utilizing mptt, [Modified Preorder Tree Traversal](https://django-mptt.readthedocs.io/en/latest/overview.html#what-is-modified-preorder-tree-traversal), making data retrieval more efficient, and allowing users (admins) to store data in hierarchical tree.

<img src="https://res.cloudinary.com/frank2021/image/upload/v1639561227/STHLM-foodies/sitepoint_tree_azmdyp.gif">

### Features to be implemented

- Automated stock control;

- Automatic delivery address on payment form, to avoid users from having to enter their delivery address twice;

- Search functionality;

- Email when orders are set to completed (i.e. items shipped);

- Add product reviews;

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)
- [Python](https://en.wikipedia.org/wiki/javascript)

### Frameworks, Libraries & Programs Used

[Django - 3.2.9](https://www.djangoproject.com/)

- Django was used as the main framework for this project

[Bootstrap 5](https://getbootstrap.com/)

- Bootstrap was used to assist with the responsiveness, styling and icons used on the website.

[Hover.css](https://ianlunn.github.io/Hover/)

- Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.

[JQuery](https://jqueryui.com/)

- This is a JavaScript framework which enables easy manipulation of the Document Object Model (DOM) using JQuery syntax.

[Google Fonts](https://fonts.google.com/)

- Google fonts was used to import the fonts into the main.css file which is used on the project.

[Cloudinary](https://cloudinary.com/)

- Cloudinary was used to store all media and static files for the project.

[Paypal](https://paypal.com/)

- Paypal is used the main payment handler for this project. In a real world scenario it allows users to pay using their paypal account or by card.

[GitHub](https://github.com/)

- GitHub is used for version control and to store the project's code after being pushed to the repository.

## Design

#### Imagery

Images used in this project were taken from [pexels](https://www.pexels.com/), and are free for use.

#### Typography

For the body elements I have chosen 'Source Sans Pro', which is easy to read and flows with the rest of the project, Sans-serif is the fallback.

## Testing

- The application has been tested on most popular browsers, including mobile versions.

### Different Browsers

- The Page does not support Internet Explorer, but has been tested in the browsers listed below using
  [Broswerstack](https://www.browserstack.com/live) tool:

|    Browser    |      Result       |
| :-----------: | :---------------: |
|    Safari     | No Problems Found |
| Safari-Iphone | No Problems Found |
|    Chrome     | No Problems Found |
|    Firefox    | No Problems Found |
|     Edge      | No Problems Found |
|     Opera     | No Problems Found |

### Further Testing

Tests were performed in a variety of different devices using different browsers, with the help of friends and family, no significant issues were found.

## Test Payments with Paypal

To demonstrate the functionality, I have added a third party application paypal as the payment management system. The payments will be taken by using one of the payment methods listed below, or by using the sandbox account provided by paypal.

|                  |                  |
| ---------------- | ---------------- |
| Card type:       | Visa             |
| Card Number:     | 4032030406952409 |
| Expiration Date: | 04/2025          |
| CVV:             | 448              |

|                  |                  |
| ---------------- | ---------------- |
| Card type:       | MasterCard       |
| Card Number:     | 5110926310812211 |
| Expiration Date: | 12/2025          |
| CVV:             | 970              |

|                  |                 |
| ---------------- | --------------- |
| Card type:       | Amex            |
| Card Number:     | 340117922777181 |
| Expiration Date: | 04/2023         |
| CVV:             | 9277            |

- Sandbox Account:

1. User: sb-lcbjg7288697@personal.example.com
2. Password: I&j/>zw0

## Validation

- This application passes all HTML and CSS validation tests.

1. [Markup Validation Service](https://validator.w3.org/)

  <img src="https://res.cloudinary.com/frank2021/image/upload/v1639571940/STHLM-foodies/validator_wb3dz0.png">

2. [ CSS Validation Service](https://jigsaw.w3.org/css-validator/)

  <img src="https://res.cloudinary.com/frank2021/image/upload/v1639570781/STHLM-foodies/2021-12-15_7_f1ayha.png">

## Forking from GitHub

When forking this project from GitHub you will need a to set up a few things in order to run this application:

1. Clone the Repository, or download the files manually from the repository;
2. Open the files in your development environment;
3. Set a Virtual Environment (On Windows - Using VScode - and making sure Python is installed)

|  #  |        In Your Terminal         |
| :-: | :-----------------------------: |
|  1  |         py -m venv venv         |
|  2  |      venv\Scripts\activate      |
|  3  | pip install -r requirements.txt |
|  4  |     py manage.py runserver      |

Create a file called env.py, in your root directory and add the following variables listed above to your file.
Once you have downloaded the Code to you machine you can follow the steps below on deployment to heroku which include instructions on how to set up the environment variables

|           Name           | Environment Variable |
| :----------------------: | :------------------: |
|    Django Secret Key     |      SECRET_KEY      |
|      CLIENT_SECRET       |    CLIENT_SECRET     |
|        CLIENT_ID         |      CLIENT_ID       |
| Heroku Postgres Database |     DATABASE_URL     |
|   Static Files Storage   |    CLOUDINARY_URL    |
|     Email Host User      |   EMAIL_HOST_USER    |
|    Default From Email    |  DEFAULT_FROM_EMAIL  |
|   App Password(Google)   |   EMAIL_HOST_PASS    |

## Deployment to Heroku

- This application has been deployed to Heroku, from a github repository. I have stored some important information
  (config vars) such as Stripe keys, email information, django secret key, database secret key on the heroku admin panel
  under config vars.

* (IMPORTANT - Don't forget to set DEBUG to False in settings.py)

1. Create the Heroku app

| #   | Step                  | Action                                                                          |
| --- | --------------------- | ------------------------------------------------------------------------------- |
| 1.1 | Create new Heroku App | APP_NAME, Location = Europe                                                     |
| 1.2 | Add Database to App   | Located in the Resources Tab, Add-ons, search and<br>add e.g. ‘Heroku Postgres’ |
| 1.3 | Copy DATABASE_URL     | Located in the Settings Tab, in Config Vars, Copy<br>Text                       |

2. Attach the Database (In your editor)

| #   | Step                                             | Action      |
| --- | ------------------------------------------------ | ----------- |
| 2.1 | Create new env.py file on top<br>level directory | E.g. env.py |

3. In env.py

| #   | Step                      | Action                                                              |
| --- | ------------------------- | ------------------------------------------------------------------- |
| 3.1 | Import os library         | import os                                                           |
| 3.2 | Set environment variables | os.environ["DATABASE_URL"] = "Paste in Heroku<br>DATABASE_URL Link" |
| 3.3 | Add in secret key         | os.environ["SECRET_KEY"] = "Make up a<br>randomSecretKey"           |

4. In heroku

| #   | Step                          | Action                        |
| --- | ----------------------------- | ----------------------------- |
| 4.1 | Add Secret Key to Config Vars | SECRET_KEY, “randomSecretKey” |

5. In settings.py

| #   | Step                                                                                                                          | Action                                                                                                        |
| --- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 5.1 | Reference env.py                                                                                                              | from pathlib import Path<br>import os<br>import dj_database_url<br>if os.path.isfile("env.py"):<br>import env |
| 5.2 | Remove the insecure secret<br>key and replace - links to the<br>secret key variable on Heroku                                 | SECRET_KEY = os.environ.get('SECRET_KEY')                                                                     |
| 5.3 | Replace DATABASES Section<br>(Comment out the old<br>DataBases Section)<br>- links to the DATATBASE_URL<br>variable on Heroku | DATABASES = {<br>'default':<br>dj*database_url.parse(os.environ.get("DATABASE*<br>URL"))<br>}                 |

6. In the terminal

| #   | Step            | Code                            |
| --- | --------------- | ------------------------------- |
| 6.1 | Make Migrations | python manage.py makemigrations |

7. In Cloudinary.com

| #   | Step                                                      | Code                      |
| --- | --------------------------------------------------------- | ------------------------- |
| 7.1 | Copy your CLOUDINARY_URL<br>e.g. API Environment Variable | From Cloudinary Dashboard |

8. In env.py

| #   | Step                                                                                     | Code                                                                 |
| --- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 8.1 | Add Cloudinary URL to env.py -<br>be sure to paste in the correct<br>section of the link | os.environ["CLOUDINARY_URL"] =<br>"cloudinary://9444:SUZi@dbhyuj5mc" |

9. In Heroku

| #   | Step                                                                                                 | Code                                                                                           |
| --- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 9.1 | Add Cloudinary URL to Heroku<br>Config Vars - be sure to paste<br>in the correct section of the link | Add to Settings tab in Config Vars e.g.<br>CLOUDINARY_URL,<br>cloudinary://9444:SUZi@dbhyuj5mc |

10. In settings.py

| #    | Step                                                                                                     | Action                                                                                                                                                                                                                                                                                                                                          |
| ---- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10.1 | Add Cloudinary Libraries to<br>installed apps                                                            | ...<br>'cloudinary_storage',<br>'django.contrib.staticfiles',<br>'cloudinary',<br>...<br>(note: order is important)                                                                                                                                                                                                                             |
| 10.2 | Tell Django to use Cloudinary<br>to store media and static files<br>Place under the Static files<br>Note | STATIC_URL = '/static/'<br>STATICFILES_STORAGE =<br>'cloudinary_storage.storage.StaticHashedCloudinaryS<br>torage'<br>STATICFILES_DIRS = [os.path.join(BASE_DIR,<br>'static')]<br>STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')<br>MEDIA_URL = '/media/'<br>DEFAULT_FILE_STORAGE =<br>'cloudinary_storage.storage.MediaCloudinaryStorage' |
| 10.3 | Link file to the templates<br>directory in Heroku<br>Place under the BASE_DIR<br>line                    | TEMPLATES_DIR = os.path.join(BASE_DIR,<br>'templates')                                                                                                                                                                                                                                                                                          |
| 10.3 | Change the templates<br>directory to TEMPLATES_DIR<br>Place within the TEMPLATES<br>array                | 'DIRS': [TEMPLATES_DIR]                                                                                                                                                                                                                                                                                                                         |
| 10.4 | Add Heroku Hostname to<br>ALLOWED_HOSTS                                                                  | ALLOWED_HOSTS =<br>["PROJ_NAME.herokuapp.com", "localhost"]                                                                                                                                                                                                                                                                                     |

11. In your editor

| #    | Step                                                  | Action                   |
| ---- | ----------------------------------------------------- | ------------------------ |
| 11.1 | Make sure to have 3 folders on top<br>level directory | media, static, templates |
| 11.2 | Create procfile on the top level<br>directory         | Procfile                 |

12. In Procfile

| #    | Step     | Action                       |
| ---- | -------- | ---------------------------- |
| 12.1 | Add code | web: gunicorn PROJ_NAME.wsgi |

13. In the terminal

| #    | Step                 | Action                                                     |
| ---- | -------------------- | ---------------------------------------------------------- |
| 13.1 | Add, commit and push | git add .<br>git commit -m “Deployment Commit”<br>git push |

14. In Heroku

| #    | Step                                       | Action                                          |
| ---- | ------------------------------------------ | ----------------------------------------------- |
| 14.1 | Deploy Content manually<br>through heroku/ | E.g Github as deployment method, on main branch |
