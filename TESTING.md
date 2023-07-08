# EliteTechPC - Testing

Here is the documentation containing all the testing carried out in this project.

## Testing Contents ##

* [Manual Testing](#manual-testing)
    * [Navbar](#navbar--screenshot)
    * [Auth](#auth--screenshot)
    * [Bag](#bag--screenshot)
    * [Checkout](#checkout--screenshot)
    * [Profile](#profile--screenshot)
    * [Admin](#admin--screenshot)
    * [Products](#products--screenshot)
    * [Footer](#footer--screenshot)
    * [Home Page](#home-page--screenshot)
    * [Contact Us](#navbar--screenshot)
* [Validators](#automated-testing)
    * [CI Python Linter](#ci-python-linter)
    * [W3C CSS Validator](#w3c-css-validations)
    * [W3C HTML Validator](#w3c-html-validations)
    * [Lighthouse](#lighthouse-tests)
    * [WAVE](#wave)
* [Bugs / Issues](#bugs--issues)

## Manual Testing ##

Here I have completed manual testing of the sites functions and accessing certain points as a user and non-user. 
I will attach the test that were done and tested by me to as much extent as I could every point of the page.

## Navbar : ![ScreenShot](./documents/testing_images/Navbar-tests-manual.png)

## Auth : ![ScreenShot](./documents/testing_images/Auth-tests-manual.png)

## Bag : ![ScreenShot](./documents/testing_images/Bag-tests-manual.png)

## Checkout : ![ScreenShot](./documents/testing_images/Checkout-tests-manual.png)

## Profile : ![ScreenShot](./documents/testing_images/Profile-tests-manual.png)

## Admin : ![ScreenShot](./documents/testing_images/Admin-tests-manual.png)

## Products : ![ScreenShot](./documents/testing_images/Products-tests-manual.png)

## Footer : ![ScreenShot](./documents/testing_images/Footer-tests-manual.png)

## Home Page : ![ScreenShot](./documents/testing_images/Homepage-tests-manual.png)

## Contact Us : ![ScreenShot](./documents/testing_images/ContactUs-tests-manual.png)

## Validators ## 


### W3C HTML Validations ### 

1. Home Page Validation Result : 
![ScreenShot](./documents/testing_images/home-page-html-validation.png)
<hr>

2. Products Page Validation Result : 
![ScreenShot](./documents/testing_images/products-page-validation.png)
<hr>

3. Products Details Validation Result : 
![ScreenShot](./documents/testing_images/product-details-validation.png)
<hr>

4. Bag Page Validation Result : 
![ScreenShot](./documents/testing_images/bag-page-validation.png)
<hr>

5. Accounts Signup Page Validation Result : 
![ScreenShot](./documents/testing_images/accounts-signup-validation.png)
<hr>

6. Accounts Login Page Validation Result : 
![ScreenShot](./documents/testing_images/account-login-validation.png)
<hr>

7. Password Reset Page Validation Result : 
![ScreenShot](./documents/testing_images/password-reset-validation.png)


### W3C CSS Validations ### 

1. Base.CSS Validation Result : 
![ScreenShot](./documents/testing_images/base.css-validated.png)
<hr>

2. Checkout.CSS Validation Result :
![ScreenShot](./documents/testing_images/checkout.css-validated.png)
<hr>


## CI Python Linter ##

* Code Institue Python linter, all these files were put through the tester and nothing of major came up. Here are the results :

![ScreenShot](./documents/testing_images/Python%20Linter%20Testing.png)


## Lighthouse Tests ##

I have completed a series of lighthouse tests for the performance of the site and other aspects.

### Home Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-homepage-desktop.png)
<hr>

### Products Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-products-desktop.png)
<hr>

### Products Details Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-product_details-desktop.png)
<hr>

### Contact Us Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-contactus-desktop.png)
<hr>

### Shopping Cart Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-bag-desktop.png)
<hr>

### Checkout Page Desktop : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-checkout-desktop.png
<hr>

### Home Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-homepage-mobile.png)
<hr>

### Products Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-products-mobile.png)
<hr>

### Products Details Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-product_details-mobile.png)
<hr>

### Contact Us Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-contactus-mobile.png)
<hr>

### Shopping Cart Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-bag-mobile.png)
<hr>

### Checkout Page Mobile : ![ScreenShot](./documents/testing_images/lighthouse_screenshots/Lighthouse-checkout-mobile.png)
<hr>

* From these tests I can see that performance wise the website could be initially improved, most likely it is due to image sizing/formats. I think with further optimizations the website can achieve fantastic results here.

## WAVE ##

I have also put the website through the WAVE accessibility testing with the following results :

![ScreenShot](./documents/testing_images/WAVE-SCREENSHOT-HOME.png)


## Website Responsiveness ##

The website has been developed to the most extent by the Front-End Library called Bootstrap. It is an amazing help towards front-end development that has a ton of features that help with the alignment of content around the website.
I have tested the website on multiple devices and it works great.
I have used the Chrome Development tools to adjust things accordingly to suit as much devices as possible.

## Bugs / Issues ##

Here I document any known to me or to anyone else that spots any bugs or issues currently going on with the site. 

1. On specially small screen sizes the text from the dropdown menu from My Account navbar , overflows off screen as it is "too long" , which really is just a visual issue.

