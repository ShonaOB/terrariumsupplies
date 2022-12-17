# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of manually testing Terrarium Supplies Ireland.

Where a feature or functionality requires the support of multiple html files, for example the mobile/main-navs supporting the index page, I have tested the homepage page in its entirety, including the footer (rather testing these files separately).

All tests were performed using the live environment deployed from Heroku on the 18/12/2022.

## User Story Testing

The objective of this test is to validate that the user requirements have been delivered.

<br>

Ref  | User Story                                                                                                                                                                                                                             | Acceptance Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Result       | Rationale                                                                                                                                                                                                                                                                                                                                                  
---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
US01 | As a Site User, I can understand what the site aim is and my options from viewing the homepage, so that I can intuitively navigate the site and have a good e-commerce experience                                                      | 1\. The site structure and layout should be clear and simple to navigate<br>2\. Site Users should be able to find products either from homepage adverts, Nav menu or Search function<br>3\. Site Users will have an option to register for a user account from the Navbar                                                                                                                                                                                                 | PASS         | This was easily achieved by user                                                                                                                                                                                                                       
US03 | As a Site User, I can use the Footer for navigation, so that I can learn more about the business                                                                                                                                       | 1\. Footer is located at the bottom of every page<br>2\. Footer provides links that are clear and accessible                                                                                                                                                                                                                                                                                                                                                                                             | PASS         | The footer contains company information, a link to contact. 
US04 | As a site user, I want to be able to create a profile page                                                                                                                                                                                                                                                                                                                                                               | PASS         | It is possible to create a profile for the user and easy to navigate                                                                                                                                                          
US05 | As a Site Owner, I can add products to the site, so I can manage the content and adapt to changes in stock and competition                                                                                                             | 1\. Successfully add a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                         | PASS         | A site owner can add new products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                                       
US06 | As a Site Owner, I can edit existing products on the site, so I can manage the content and adapt to changes in stock and competition                                                                                                   | 1\. Successfully edit a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                        | PASS         | A site owner can edit existing products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                                 
US07 | As a Site Owner, I can remove products from the site, so I can manage the content and adapt to changes in stock and competition                                                                                                        | 1\. Successfully remove a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                      | PASS         | A site owner can remove existing products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                               
US08 | As a Site User, I can learn about a product from the details provided, so that I can make an informed decision to purchase                                                                                                             | 1\. Sufficient details on the product pages<br>2\. Product page with full descriptions in addition to those highlighted in 1.                                                                                                                                                                                                                                                                        | PASS         | Every product can be viewed in isolation complete with a subtitle and description. Other key pieces of information are contained within the product details page such as  price.                                                                                                                                                   
US09 | As a Site User, I can easily navigate to the differing product lines by using clear and conventional categories, so that I can find specific items with ease, and move between sections of the shop                                    | 1\. Category views that are accessible from the Navbar menu<br>2\. Category views that correctly filter.<br><br>                                                                                                                                                                                                                                                                                                                                                                           | PASS         | Drop-down menus from the fixed Navbar allow users to navigate to specific categories or see all products.                                                                                                                                                                                                                      
US15 | As a Site User, I can view recommendations from existing customers, as it will help to inform my trust in the business                                                                                                                 | 1\. Reviews available on product pages                                                                                                                                                                                                                                                                                                                                                                                               | PASS         | Product reviews are enabled for all products. To leave a review you must be registered and have verified the account through email confirmation.                                                                                                                                                                                                                                                                                   
US18 | As a Site User, I would like to make a transaction without registering for a user account, as this is either a one off purchase or is my preference not to have a company hold my details                                              | 1\. Not registered users can checkout without an account whilst still maintaining all checkout functionality<br>                                                                                                                                                                                                                                                                                                                                                                                         | PASS         | Site users can checkout without being a registered user.                                                                                                                                                                     
US20 | As a Site User, I would like to adjust the quantity or remove items from my shopping bag, in case I change my mind when assessing all my items before purchasing                                                                       | 1\. Site Users can increase or decrease the quantity of items within them shopping bag as part of the checkout process                                                                                                                                                                                                                                                                                                                                                                                   | PASS         | Site users have the functionality to increase or decrease items within their bag before checking out. Users can also remove items completely.                                                                                                                                                                                                              
US21 | As a Site User, I can register an account, so that I can add reviews                                                                                                                                                                   | 1\. Site Users are provided with a simple Form to complete in order to register an account<br>2\. Form fields should follow convention for sign-up forms<br>3\. Form buttons should enable the Form to be submitted or reset if an error has been made                                                                                                                                                                                                                                                   | PASS         | Users can sign-up for an account using a simple form and following instructions within to verify their account.                                                                                                                                                                                                                                            
US22 | As a Site User, I can sign-in to my account                                                                                                           | 1\. Site Users will be able to sign-in from clicking a link in the Navbar menu<br>2\. Sites Users will be required to enter their Username and Password to sign-in<br>3\. A message should confirm to Site Users when they have successfully signed in<br>4\. A message should inform Site Users if the information entered was not valid, and to try again                                                                                                                                              | PASS         | Site users can register for an account. Whilst for MVP the features are limited to storing default delivery details and viewing previous transactions, further benefits can be introduced for later releases as the foundations are built.                                                                                                                 
US23 | As a Site User, I can be asked to confirm my request to sign-out, so that I can cancel if requested in error                                                                                                                           | 1\. Site Users will be able to sign-out from clicking a link in Navbar menu<br>2\. A page will display asking Site Users to confirm they would like to proceed to sign-out, or continue using the site<br>3\. If Site Users confirm they would like to sign-out they will be signed out and redirected to the home page<br>4\. A message should confirm to Site Users when they have successfully signed out<br>5\. If Site Users choose to continue using their account, access to features will remain | PASS         | Using the inbuilt functionality of Django, users are asked to confirm their request to sign-out.                                                                                                                                                                                                                                                           
US24 | As a Site User, I can view and change profile details, so that they are correct when I come to checkout                                                                                                                                | 1\. Site Users can navigate to a restricted page that provides all the relevant profile details<br>2\. Site Users can amend any part of the information and save the changes<br>3\. A success message will confirm the changes have been saved                                                                                                                                                                                                                                                           | PASS         | Registered site users can edit their default delivery details within the profile area. A success message confirm the changes have been saved.                                                                                                                                                                                                              
US25 | As a Site User, I can add a product review, so that I can inform potential customers of what they might expect<br><br>                                                                                                                 | 1\. Authenticated users will be able to post a review on a detailed product page<br>2\. A button clearly stating to 'Submit' their review will be available<br>4\. Site Users will be able to see their post instantly<br>                                                                                                                                                                                                            | PASS         | Registered site users can add a product review directly to the website. Consideration was given to adding an approval step before publishing the comment, however to provide a positive user experience, I opted to publish the review straight away. These can be reviewed by the business owner and deleted from the Django admin area if deemed abusive.
US30 | As Site Owner, I would like Site Users to register for a monthly newsletter, so that I can build a relationship with customers and promote specific products                                                                           | 1\. Site User can enter an email address and receive a success message within the browser<br>2\. Site Users will receive confirmation of sign-up to their inbox                                                                                                                                                                                                                                                                                                                                          | PASS         | Site users can subscribe to the newsletter using the Mailchimp feature on the homepage. Users do not have to register to subscribe and stay updated with products and news.                                                                                                                                                                        
US32 | As Site Owner, I can provide a contact form for Site Users, so they can provide feedback, request products, features etc.                                                                                                              | 1\. Site Users will be able to access this page from the main nav<br>2\. Site Users will be provided with a Form to complete, learning where the Form is sent and when to expect a response<br>4\. Site Users will be redirected to the homepage when the form has been successfully submitted                                                           | PASS         | There is a contact form available for Site Users to send a query, concern or request to the business owners.<br>Feedback is provided to the users to confirm the form has been sent successfully.                                                                                                                                                                                                                                                                                                                                                                                                             
US37 | As a Site User, I can access the site on differing devices, so I can interact with content on my preferred device                                                                                                                      | 1\. Successful tests for Responsiveness using Developer Tools<br>2\. Successful tests for Responsiveness through manual testing on differing devices                                                                                                                                                                                                                                                                                                                                                     | PASS         | Primarily using the Bootstrap framework the website is responsive across devices. This has been tested through a dedicated test for responsiveness.                                                                                                                                                                                                        
US02 | As a Site User, I can search for products by entering descriptive words, so that I can find what I want quickly                                                                                                                        | 1\. Search functionality is accessible from the Navbar<br>2\. All keywords, names, descriptions return results                                                                                                                                                                                                                                                                                                                                                                                           | PASS | Search functionality is working as expected.                                                                                                                                        

<br>

## User Acceptance Testing

To ensure the website is meeting real world expectations, I asked other developers to review and feedback on their user experience. 

These tests provided rich insight into the practicalities and behaviours of the features and functions. From the issues identified (below) I will change some features to improve the user experience ahead of MVP release.

1. Whilst the user enjoyed the success feedback from leaving a product review, they felt it was strange to choose any product from the dropdown, whether they have purchased it previously or not. This will be included in a future release. 
1. The use of a product rating is not functional fully - as the review process does not calculate a rating or adjust the product rating. I will research further into this and amend in the future release. 
1. Users wanted to create a wishlist, and to build a "kit" that they could purchase. I will review this possibility for the next release. 

<br>


## Page Validation

This test aims to check all features and links from across the site are working as designed and developed.

To perform the test I used a Chrome browser, and validated each page from a mobile and desktop perspective using the inbuilt developer tool as some features were unique to a particular screen size.

The results were largely positive with two noticeable fails:
* The custom 404 error page does not appear to be loading - this will require further investigation. 
* the custom 500 page error does not appear to be loading - this will require further investigaion. 

<br>

File path                                                                                    | Features working | Links active
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS        
checkout/templates/checkout/checkout\checkout_success.html                                   | PASS             | PASS        
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS        
communications/templates/communications.html                                                 | PASS             | PASS      
[https://terrariumsupplies.herokuapp.com//](https://terrariumsupplies.herokuapp.com/)        | PASS             | PASS        
home/templates/home/index.html                                                               | PASS             | PASS
products/templates/products/add_product.html                                                 | PASS             | PASS        
products/templates/products/edit_product.html                                                | PASS             | PASS        
products/templates/products/product_detail.html                                              | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/confirm-email.html                                                 | PASS             | FAIL        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS        
templates/errors/404.html                                                                    | PASS             | FAIL        
templates/errors/500.html                                                                    | PASS             | FAIL        
reviews/templates/update_review.html                                                         | PASS             | PASS
reviews/templates/reviews.html                                                               | PASS             | PASS

<br>


## Responsiveness

To test the websites layout and content remains well structured and accessible across differing screen sizes, I used Chrome's Developer Tools to virtualise how the website and all it's pages look and feel. In consideration that I opted to use Bootstrap which provides standard media queries for screen sizes from XS through to XL, I selected the following screens to test on; iPhone 4, iPhone SE, Samsung Galaxy S8, iPad, iPad Pro, Laptop at 1366x768, Monitor at 1920x1080 and iMac 5K.

All Pages working as expected. 

<br>

File path                                                                                    | Dev tools Pass   | WAVE Pass
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS        
communications/templates/communications.html                                                 | PASS             | FAIL - form      
[https://terrariumsupplies.herokuapp.com//](https://terrariumsupplies.herokuapp.com/)        | PASS             | PASS        
home/templates/home/index.html                                                               | PASS             | PASS
products/templates/products/product_detail.html                                              | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS        
reviews/templates/reviews.html                                                               | PASS             | PASS

<br> 

## Accessibility 


In summary of the results;
* Given the nature of the Django build, I tested the live web page as opposed to the code input validation method. This was successful.
* The forms for managing products came under scrutiny as they are not supported by screen readers as standard and hence received a sub 90% score. For a future release the forms will be rebuilt to ensure compliance. 
* Within the homepage some mailchimp features were missing tags, which were resolved. 
* The inclusion of the third party element in MailChimp raised an a couple of errors including contrast, which were resolved as much as possible.
<br>

bag/templates/bag/bag.html                                                                   | PASS             | PASS        
checkout/templates/checkout/checkout\checkout_success.html                                   | PASS             | PASS        
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS        
communications/templates/communications.html                                                 | PASS             | PASS      
[https://terrariumsupplies.herokuapp.com//](https://terrariumsupplies.herokuapp.com/)        | PASS             | PASS        
home/templates/home/index.html                                                               | PASS             | PASS
products/templates/products/add_product.html                                                 | PASS             | PASS        
products/templates/products/edit_product.html                                                | PASS             | PASS        
products/templates/products/product_detail.html                                              | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/confirm-email.html                                                 | PASS             | PASS        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS        
templates/errors/404.html                                                                    | PASS             | PASS        
templates/errors/500.html                                                                    | PASS             | PASS        
reviews/templates/update_review.html                                                         | PASS             | PASS
reviews/templates/reviews.html                                                               | PASS             | PASS

<br>

## Code

Writing well formed, quality code is essential for the future development of any website. TI have used industry standard tools [list below] to validate every line of code using the input method. As well as using this tools, using GitPod as IDE allowed me to utilise the inbuilt code checkers such as Pycodestyle for Python. 

* W3 Validator for HTML
* W3 Jigsaw for CSS
* JS Hint for JavaScript
* CI Python Linter for Python

To gain passes across the code base I had to address minor issues such as;

* General formatting and resolving E501 line length errors
* Removing unnecessary trailing slashes from elements e.g. <br/>
* Removing unnecessary 'type' attribute from script tags
* Remove an anchor tag from within a HTML button and change the anchor to look like a button.
* Adding new lines to the end of Python files to resolve W292 errors.
* More details of these minor infringements can be found within the (TCC Testing document in the repo)[].

The following issues were identified and not resolved so carry an EXC = pass with an acceptable exception.

* env.py - E501 as line breached 79 characters, however when I tried to split the Database URL over two lines it not longer functioned. As a result I have chosen to allow this exception for the MVP.
* profiles.js and stripe_elements.js - ES6 warning to use 'esversion:6'. I researched a fix and added JSHint ES6 to the settings.JSON file, however this did not clear the warning. As this was a warning and I could not identify any issues with functionality I chose to allow this exception for the MVP.

<br>

| File path                                                                                    | File Type | HTML | CSS  | JavaScript | Python | GitPod errors |
| -------------------------------------------------------------------------------------------- | --------- | ---- | ---- | ---------- | ------ | ------------- |
| bag/static/css/bag.css                                                                       | CSS       |      | PASS |            |        | PASS          |
| bag/templates/bag/includes/bag-total.html                                                    | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/checkout-buttons.html                                             | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/product-image.html                                                | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/product-info.html                                                 | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/quantity-form.html                                                | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/bag.html                                                                   | HTML      | PASS |      |            |        | PASS          |
| bag/templatetags/bag\_tools.py                                                               | PY        |      |      |            | PASS   | PASS          |
| bag/apps.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| bag/contexts.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| bag/urls.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| bag/views.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| checkout/static/css/checkout.css                                                             | CSS       |      | PASS |            |        | PASS          |
| checkout/static/js/stripe\_elements.js                                                       | JS        |      |      | EXC        |        | PASS          |
| checkout/templates/checkout/checkout\_success.html                                           | HTML      | PASS |      |            |        | PASS          |
| checkout/templates/checkout/checkout.html                                                    | HTML      | PASS |      |            |        | PASS          |
| checkout/admin.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| checkout/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/models.py                                                                           | PY        |      |      |            | PASS   | EXC           |
| checkout/signals.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| checkout/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| checkout/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/webhook\_handler.py                                                                 | PY        |      |      |            | PASS   | EXC           |
| checkout/webhooks.py                                                                         | PY        |      |      |            | PASS   | EXC           |
| company/static/css/company\_pages.css                                                        | CSS       |      | PASS |            |        | PASS          |
| company/templates/accessibility\_statement.html                                              | HTML      | PASS |      |            |        | PASS          |
| company/templates/contact.html                                                               | HTML      | PASS |      |            |        | PASS          |
| company/templates/copyright\_statement.html                                                  | HTML      | PASS |      |            |        | PASS          |
| company/templates/faqs.html                                                                  | HTML      | PASS |      |            |        | PASS          |
| company/templates/health\_benefits.html                                                      | HTML      | PASS |      |            |        | PASS          |
| company/templates/our\_story.html                                                            | HTML      | PASS |      |            |        | PASS          |
| company/templates/sustainability.html                                                        | HTML      | PASS |      |            |        | PASS          |
| company/templates/terms\_and\_conditions.html                                                | HTML      | PASS |      |            |        | PASS          |
| company/admin.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| company/apps.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| company/forms.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| company/models.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| company/urls.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| company/views.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | HTML      | PASS |      |            |        | PASS          |
| home/apps.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| home/urls.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| home/views.py                                                                                | PY        |      |      |            | PASS   | PASS          |
| products/static/css/products.css                                                             | CSS       |      | PASS |            |        | PASS          |
| products/templates/products/custom\_widget\_templates/custom\_clearable\_file\_input.html    | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/includes/quantity\_input\_script.html                            | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/add\_product.html                                                | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/delete\_product\_page.html                                       | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/edit\_product.html                                               | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/product\_detail.html                                             | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/products.html                                                    | HTML      | PASS |      |            |        | PASS          |
| products/admin.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| products/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/models.py                                                                           | PY        |      |      |            | PASS   | PASS          |
| products/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| products/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/widgets.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| profiles/static/css/profiles.css                                                             | CSS       |      | PASS |            |        | PASS          |
| profiles/static/js/profiles.js                                                               | JS        |      |      | EXC        |        | PASS          |
| profiles/templates/profiles/profile.html                                                     | HTML      | PASS |      |            |        | PASS          |
| profiles/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| profiles/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| profiles/models.py                                                                           | PY        |      |      |            | PASS   | PASS          |
| profiles/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| profiles/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| static/css/style.css                                                                         | CSS       |      | PASS |            |        | PASS          |
| tcc/settings.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| tcc/urls.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| tcc/views.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| tcc/wsgi.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| templates/allauth/account/confirm-email.html                                                 | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/login.html                                                         | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/logout.html                                                        | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/signup.html                                                        | HTML      | PASS |      |            |        | PASS          |
| templates/errors/403.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/404.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/405.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/500.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_error.html                                                  | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_info.html                                                   | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_success.html                                                | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_warning.html                                                | HTML      | PASS |      |            |        | PASS          |
| templates/includes/footer.html                                                               | HTML      | PASS |      |            |        | PASS          |
| templates/includes/main-nav.html                                                             | HTML      | PASS |      |            |        | PASS          |
| templates/includes/mobile-top\_head.html                                                     | HTML      | PASS |      |            |        | PASS          |
| templates/base.html                                                                          | HTML      | PASS |      |            |        | PASS          |
| custom\_storages.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| env.py                                                                                       | PY        |      |      |            | PASS   | EXC           |


<br>


## Bugs

The following bugs were identified as part of the testing phase and will be investigated further to find a fix.

### Bugs that require a fix for MVP

**B1.** As a site admin performing a product delete from the front end, a 500 Internal Server Error was triggered after clicking submit on the final screen. This requires further investigation. **FIXED** - The URL path and View functionality required updating to ensure the right action occurred when the 'Delete' input was clicked from within the form. All aspects of this feature have been updated and tested successfully.<br>
**B2.** A link contained on the Our Story page to navigate users to sign-in/register is broken as it directs users to the homepage. **FIXED** - dynamic URL has been revised to link to the correct sign-up page.<br>

### Bugs that require further investigation and potentially fixed for MVP

**B3.** Decouple the bag details from the toast success - so that a bag toast is only displayed when adding or removing items from the bag. This will improve the users experience through clearly feeding back on how they are interacting with the site. **INVESTIGATION UPDATE** - Internet forums and the documentation for Bootstrap and Django are suggesting the use of the inbuilt messaging functionality is limited and therefore creating a second 'success' message would confuse the system and it wouldn't be callable. Further development will be required for a future release that moves away from this feature to create custom messages that are called uniquely with JavaScript. This will ensure the bag items are not in view when leaving a review on the product page.<br>
**B4.** Centralise the image of Luca and text from the homepage on mobile devices - so that it follows the format of the business location and opening times above. **FIXED** - CSS updated for this section to centralise the image and text for screens smaller than 768px wide.<br>
**B5.** Investigate why search results are not found when entering more than one descriptive word, or not returning results as expected. **UPDATE** - The query method appears to be working as intended and has code to consider values separated by a ','. I attempted to increase the product model fields that were queryable however I started to encountered FieldErrors which I could not resolve through the use of StackOverflow. Furthermore the [Django Documentation](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_search_results) suggests that for versions pre 4.1, results can only be returned on the values from the same relational row, and not from any rows that may carry any one of the searched values. Further investigation post MVP with an upgrade to version 4.1 potentially.<br>
**B6.** To avoid user confusion, consider removing the product rating unless we can provide functionality for users to interact with the rating. Possibly change this to a 'like' system which would provide a method for leaving quick feedback.<br>
**B7.** The use of the 'Coffee Intensity' field as a method of sorting products works well if sorting coffee products. However it loses its value and is a little misleading for non-coffee products. To fix I will investigate whether we can limit the displaying of this field to only show on the coffee relating pages, otherwise it may be clearer to remove as a sorting options. **UPDATE** - I've performed some testing around the sorter and feel the option to have this field within the sorting options still provides value. I've tried to use for loops with the coffee category to only show the 'Coffee Intensity' options when those products view, however I could not successfully get the for loop to work for the MVP release date.<br>
**B8.** The homepage initial load on mobiles is scoring poorly on Chromes Developer Tools. Investigate whether resizing images will improve page loading times for mobiles. **UPDATE** - Right-sized images have been introduced through the use of a picture tag. Whilst it has helped marginally to improve the Lighthouse performance score, it has not been a significant improvement. Attempting to defer script loadings as part of the original tests were also not successful. Further investigation is required to understand the guidance steps proposed as part of the Lighthouse test results.<br>


### Bugs that won't be fixed for MVP

**B9.** There was one isolated issue whereby the inherit styles for the Mailchimp element didn't load completely correct on my local machine when using Firefox. This also included the 'Subscribe' button not being functional. I tried to replicate this virtually using Firefox within the Lambda tool, however the feature loaded correctly and was functional.<br>
**B10.** env.py code error - E501 as line breached 79 characters, however when I tried to split the Database URL over two lines it not longer functioned. As a result I have chosen to allow this exception for the MVP.<br>
**B11.** profiles.js and stripe_elements.js code errors - ES6 warning to use 'esversion:6'. I researched a fix and added JSHint ES6 to the settings.JSON file, however this did not clear the warning. As this was a warning and I could not identify any issues with functionality I chose to allow this exception for the MVP.<br>