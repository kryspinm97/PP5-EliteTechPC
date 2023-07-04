# EliteTechPC #

* Here I have created EliteTechPC - Prebuilt Computers which is a B2C e-commerce site. The site allows the users to have a look around for their next potential home office pc, a workstation for heavy duty work or even a high performance gaming machine. There is loads of features currently implemented into the website with more to come.
Registered users gain access to My Profile which lets them update their delivery information and track their orders.

<hr>

![ScreenShot](./documents/readme_images/AmiResponsiveImg.png)

The live version of the website is available for you here : <a href="https://elite-tech-pc-e966cb86c987.herokuapp.com/">EliteTechPC</a>

# README CONTENTS # 

<hr>

* ## [UX](#ux-1)
   * [User Stories](#user-stories)
   * [Agile Methodologies](#agile-methodologies)
   * [The Scope](#1-scope)
   * [Structure](#2-structure)
   * [Skeleton](#3-skeleton)
   * [Surface](#4-surface)

* ## [Credits](#credits-1)

<hr>

# UX #

## User Stories ##

  * Site Owner Goals : 
  
    * Create a visually appealing and professional website design to attract users
    * Implement a user-friendly and intuitive interface for easy navigation
    * Enable user account management and access control
    * Provide tools for managing and moderating user-generated content
    * Develop a responsive design that works seamlessly on various devices
    * Establish effective communication channels to interact with users and offer support.

  * User Goals : 

    * Allow users to create accounts and have control over their information
    * Provide a straightforward and efficient browsing experience for content discovery
    * Delivery a responsive and user-friendly design that functions well on all devices
    * The ability to add/edit/remove/update items in the shopping cart

By addressing these goals, EliteTechPC aims to create a compelling and user-centric experience for both the site owner and the users, satisfaction and a seamless interaction with the platform.

<hr>    

## Agile Methodologies ##

<hr>

The Agile Methodology approach was adopted during the development of the EliteTechPC - E-Commerce Prebuilt PC store. I have utilized GitHub's built-in features such as issue tracking and project management to effectively manage tasks and monitor progress.

User stories were categorized into "Must-Have" and "Could-Add" features to prioritize the development process. This allowed for systematic approach to implementing essential functionalities while leaving room for future enhancements.

While the application is still a work in progress, it is continuously evolving with a focus on delivering a fully functional and feature-rich online store for users to explore. I remain dedicated to expanding the platforms capabilities and provide an exceptional shopping experience for customers.

<hr>

## 1. Scope ## 

EliteTechPC is an E-Commerce website offering a wide range of prebuilt computers. The scope of this project is to develop a fully functional and user-friendly online store that allows customers to browse, purchase, and manage their orders seamlessly.

<hr>

## 2. Structure ##

* Features and Functionality :
    * User Registration and Authentication :
        * User registration and login functionality for customers to create and manage their accounts.
        * User authentication and access control to ensure secure and personalized experiences.
    * Product Catalog :
        * Display a comprehensive catalog of prebuilt computers.
        * Categorize products based on different criteria such as, prize, name , ratings etc.
        * Provide detailed product information, including specifications, images and ratings.
    * Shopping Cart and Checkout :
        * Enable customers to add products to their shopping cart and manage quantities.
        * Implement a secure and intuitive checkout process, including address and payment information collection.
        * Integration with payment gateway to facilitate secure online transactions (Stripe).
    * Order Management :
        * Allow users to view and track their order history, including the order number, date, total cost and item.
    * Search and Filtering :
        * Implement a search functionality to allow customers to find products based on keywords or specific criteria
        * Enable filtering options to refine product search results based on various attributes.
    * Responsive Design :
        * Develop a responsive website that provides optimal user experience across different devices and screen sizes.
        * Ensure seamless navigation and readability on desktops, tablets and mobile devices.
    * Admin Panel :
        * Implement an admin panel for site administrators to manage products, orders and user accounts.
        * Enable inventory management, including stock updates and product additions or removals.
    

<hr>

## 3. Skeleton ##

Here is a basic wireframe of the website's layout : 
![ScreenShot]()

Here is the database schema for the project : 
![ScreenShot]()

<hr>

## 4. Surface ## 

The design of CarStyleAutos is clean and modern, with a focus on readability and ease of use. The color scheme consists primarily of black,white, shades of gray, with red accents used sparingly for emphasis.


## Colors :

Here's the primary pallete of colors I have used throughout this project.
These are vibrant colors that I think offset each other really and work together. 

![ScreenShot](./documents/readme_images/Colors-Pallete.png)


## Layout -

The layout of the EliteTechPC website is designed to be responsive and user-friendly across various devices thanks to Bootstrap! The website utilizes the Bootstrap framework to ensure a consistent and visually appealing experience. The layout elements are :

1. Header:
    * The header section is sticky to the top of the screen, providing easy navigation and access to essential features wherever you may be on the page.
    * The EliteTechPC logo is prominently displayed, along with navigation links to different sections of the website.
    * The header also includes additional elements such as a search barm user account options and a shopping cart.

    * ![ScreenShot]()

2. Hero Section:
    * The Hero section showcases a visually appealing image related to the computer hardware for PC's 
    * It features a compelling headline and a call-to-action button to encourage users to start to explore the products the website has to offer.

    * ![ScreenShot]()

3. Product Display:
    * Products are presented in a grid format, allowing users to browse through different categories and options.
    * Each product listing includes key information such as product name, image, price and rating.
    * Users can click on a product to view more details including specifications and a quantity input for however amount of items they desire.

    * ![ScreenShot]()

4. Shopping Cart and Checkout:
    * A user friendly shopping cart interface allows customers to add products, adjust quantities and proceed to checkout.
    * The checkout process includes collecting necessary information like shipping address and payment details.
    * Users are guided through the steps and provided with clear instructions to complete their purchase securely.

    * ![ScreenShot]()

5. Content Cards: 
    * Content cards are utilized throughout the website to present various information such as featured products, categories etc.

    * ![ScreenShot]()

6. Footer:
    * The footer section appears at the bottom of the page , featuring essential site information such as contact details and links to important pages.

    * ![ScreenShot]()

Overall, EliteTechPC website layout aims to provide a visually appealing and intuitive user interface, ensuring that users can easily navigate, explore and engage with the range of prebuilt computers offered by the store.

<hr>

# Testing # 

 * I have created a seperate markdown documentation for the testing of this project. 

 - You can view the testing here : [Testing.MD](./TESTING.md)

 <hr>

# Deployment #

* ## Heroku.com Service ##

  * Here we log in or create an account to begin with.
  * On the dashboard view click 'Create New App' from the dropdown menu
  * Choose your app-name and region
  * Setup the CONFIG_VARS in the Settings tab in your project. 
      * SECRET_KEY
      * DATABASE_URL

      These three url's are to be set up and configured in your project.
      These connect your Database , Cloudinary and your Django Enviroment Key.
  * In the buildpack section in the settings tab add Python , then save changes.
  * Last but not least Link your project under the Deploy tab by selecting it from your github repository.

* ## Final Steps #

  * Make sure your settings.py option DEBUG = True is set to FALSE.
  * Ensure you have your Procfile created with the following code :
      * web: gunicorn carstyleautos.wsgi


* You can find the deployed version of the website here : <a href="https://carstyleautos-blog.herokuapp.com" target="_blank">CarStyleAutos</a>

<hr>

# Technologies Used #

* ## Languages ##
  * HTML
  * CSS
  * Python
  * JavaScript

* ## Frameworks / Libraries / Programs ##
  * <a href="https://www.djangoproject.com/">Django (Python web Framework)</a> 
  * <a href="https://jquery.com/">jQuery (Javascript Library)</a>
  * <a href="https://getbootstrap.com/">Bootstrap (Front-End Library)</a>
  * <a href="https://django-crispy-forms.readthedocs.io/en/latest/">Django-Crispy-Forms (Django Form Rendering Library)</a>
  * <a href="https://pypi.org/project/psycopg2/">Psycopg2-Binary(PostgreSQL database adapter for Python)</a>
  * <a href="https://balsamiq.com/wireframes/?gclid=CjwKCAjw0N6hBhAUEiwAXab-TS4-B3FwE_NpeSWRL6jqqSJMnuxinyknl1t_ddtaW_Jd3UAOvbxguhoC4agQAvD_BwE">Balsamiq Wireframes(Wireframe Software to sketch initial design)</a>
  * <a href="https://github.com/">GitHub (Version Control alongside a Local Development Enviroment)</a>
  * <a href="https://fontawesome.com/">Font Awesome (Library of Icons)</a>
  * <a href="https://www.elephantsql.com/">ElephantSQL (Hosting service for the database for this application)</a>
  * <a href="https://aws.amazon.com/">AWS Amazon Hosting Service</a>
  * <a href="https://heroku.com/">Heroku (Application hosting service)</a>
  * <a href="https://www.lucidchart.com/pages/">Lucidchart (Online Application for Flowcharts/Diagrams)</a>

<hr>

# Credits #

### Coding ###

* <a href="https://google.com">Google</a>
* <a href="https://ui.dev/amiresponsive">AMI Responsive</a>
* <a href="https://stackoverflow.com/">Stack Overflow</a>
* <a href="https://youtube.com">YouTube</a>
* <a href="https://w3schools.com">W3Schools</a>
* <a href="https://https://codeinstitute.net/">Code Institute</a>
* <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">Boostrap Documentations</a>

* All those resources were very valuable in the progression of my project whenever I was stuck at any point in time I refered back to the course material as well as the online resources.

* All my images were sourced from google images, and any copyrights are reserved for the owners as these are just for display purposes only.


### I would like to thank Code Institute for supplying me with the necessary guidance for this project. And Tutor support for certain things I was completely stuck at.

[def]: #credits