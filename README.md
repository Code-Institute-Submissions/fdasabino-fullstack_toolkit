# STHLM-foodies - Fresh food delivered to your door

<img src="">

[Deployed Application](https://sthlm-foodies.herokuapp.com/)

## Project Goals

- This page was designed with the intent to create a e-commerce website that allows B2C interactivity.
  Showing the skills required in order to fullfil the requirements of the project milestone number 4 of the Code Institute and it's leaning outcomes.

## UX

- This application was developed to host a multi-product store, that can accommodate a variety of products.
  In the section below you will find our user stories and some more information about the user experience and how users can interact with this website.

### Visitors can

- Browse around the website and for products.
- See products lists and categories allowing faster and smoother ordering.
- Register on the website.
- Manage personal accounts, change addresses and password.
- Delete their personal accounts

### User Stories

- As an user wish to make a purchase directly from the website.
- As a customer I wish to find relevant information about a specific product.

### Site Owner Goals

### First Time Visitor Goals

1. As a First Time Visitor, I want to easily understand the main purpose of the page and navigate to the section I need.
2. As a First Time Visitor, I want to be able to look at products and add them to my favorites before I decide to purchase them.

### Returning Visitor Goals

1. As a Returning Visitor, I want to find updated products and offers on the homepage.
2. As a Returning Visitor, I want to log in and log out into my account and manage my details.

## Existing Features

- This application was divided in 5 main components, that are connected, and are responsible for a different set of features on the application:

#### Account

- This application is responsible for all account related features, login, logout, account creation and deletion, password changes and so on.
  I have utilized some templates provided by django allauth, but have overridden the main auth functionality by creating a CustomAccountManager class
  based on the django-allauth model.

#### Basket

- The basket application handles all the basket related features such as add, update and remove items. This feature was built using the browser session to
  hold product data. This application works hand in hand with the checkout and order application.

#### Checkout

#### Order

#### Store

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)
- [Python](https://en.wikipedia.org/wiki/javascript)

### Frameworks, Libraries & Programs Used

[Django - 3.2.9](https://www.djangoproject.com/)

- Django was used as the main framework for this project

[Bootstrap 5 :](https://getbootstrap.com/)

- Bootstrap was used to assist with the responsiveness, styling and icons used on the website.

[Hover.css:](https://ianlunn.github.io/Hover/)

- Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.

[JQuery](https://jqueryui.com/)

- This is a JavaScript framework which enables easy manipulation of the Document Object Model (DOM) using JQuery syntax.

[Google Fonts:](https://fonts.google.com/)

- Google fonts was used to import the fonts into the main.css file which is used on the project.

[Cloudinary:](https://cloudinary.com/)

- Cloudinary was used to store all media and static files for the project.

[Paypal](https://paypal.com/)

- Paypal is used the main payment method for this project. In a real world scenario it allows users to pay using their paypal account or by card.

[GitHub:](https://github.com/)

- GitHub is used for version control and to store the project's code after being pushed to the repository.

## Test Payments with Paypal

- To demonstrate the functionality, I have added a third party application paypal as the payment management system. The payments will be taken
  by using one of the payment methods listed below, or by using the sandbox account provided by paypal.

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
