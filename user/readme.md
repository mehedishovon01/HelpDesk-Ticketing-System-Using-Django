# User
This readme is only for the user. This will show the process of user's Models, Form, Views and all the details

## Topic Coverd
1. Class under class (inner class, enumeration class)
2. How to use Choices in Model and Forms
3. By default fullname
4. __str__ & __unicode__ er difference and python3 is no __unicode__ method 
5. Using Auto_now_add & auto_now 
7. Timezone using
8. List_display in the row of the table in django-admin
9. Readonly_fields display the hidden field in django-admin form details


# In Models
Here is the details of the model in django and Uses the models class in this project.<br>
A model is a Python class that represents a database table. It defines the fields of the table and their respective data types, constraints, and behaviors. Models are a fundamental part of Django's Object-Relational Mapping (ORM) system.

Key aspects of a Django model:
#### Model Class:
* A Django model is defined as a Python class that inherits from django.db.models.Model.

#### Fields:
* Fields define the structure of the database table. They specify the type of data that can be stored in a particular column.

#### Relationships:
* Models can establish relationships with other models, such as ForeignKey for many-to-one relationships or ManyToManyField for many-to-many relationships.

#### Methods:
* Models can have methods to perform specific actions related to the data in the table.
* The __str__ method, for example, is often defined to provide a human-readable representation of model instances.

#### ORM:
* Django's ORM allows to interact with the database using Python code rather than writing SQL queries.

#### Migrations:
* Django models are used in conjunction with migrations, which are files that track changes to the database schema.

## Def user_str
This function is used for return the User's First & Last Name by default.

In Python 3, there is no __unicode__ method. Instead, use the __str__ method for string representation. Python 3 uses Unicode by default for string handling.

## Class ProfileDetails Model
This class is for store the details of user's information with the a foreign key from User.

Defining this class is meant to store information related to a user's profile. Additionally, here defined an inner class named GenderChoices MaritailChoices within the ProfileDetails model, and it inherits from models.TextChoices. This inner class is used to define choices for the gender and martail_status field.
> Name_of_the_Class: inner class

## Class GenderChoices & MaritailChoices Enumeration Class
Thoes classes are represents a Django model (ProfileDetails) with an enumeration (GenderChoices & MaritailChoices) for defining choices related to the gender field within that model.

Thoes classes are an enumeration class that defines choices for the gender field in the ProfileDetails model. Each choice is represented as a pair of a human-readable name (e.g., 'Male') and its corresponding value (e.g., 'Male'). By using an enumeration, it easier to manage and reference the available choices for the gender field.
> values: string literals <br>
> Name_of_the_Class: enumeration class


# In Forms
A form is a high-level representation of an HTML form on the server side. It allows you to define the fields in a form, specify their types, and add validation rules. Django forms simplify the process of collecting and validating user input from web forms, and they play a crucial role in handling user interactions in web applications.

#### Key features and concepts
1. Form Classes:
2. Fields
3. Validation
4. Rendering HTML
5. Handling Submissions
6. Model Forms
6. CSRF Protection
7. Widgets

## class UserRegisterForm
This class is for User registration form. Where Phone Number Can Added

## class UserUpdateForm
User Update form. Where user can update their Name & email

## class ProfileUpdateForm
User Update form. Where user can update their profile details

# In Views

## def registration
This function handles user registration by processing the registration form.
If the user's http method is POST then it will create a new user otherwise it will show a registration from.
HTTP Method: POST

## def change_password
This function allows a logged-in user to change their password.
If the form is valid then save the form to update the user's password. Update the session authentication hash. Display a success message.
And redirect the user back to the 'change_password' page. Otherwise, display an error message.
HTTP Method: POST

## def dashboard
This function renders the dashboard page for a logged-in user.
It must needed to login user.
HTTP Method: GET

## def profile
This function allows a logged-in user to update their profile information.
If method is POST then Validate the submitted user update form (UserUpdateForm) and profile update form (ProfileUpdateForm).
If both forms are valid save the user update form to update user details. Save the profile update form to update profile details.
Redirect the user back to the 'profile' page. 
And If not POST: Create instances of UserUpdateForm and ProfileUpdateForm for rendering the profile update form.
It must needed to login user.
HTTP Method: POST
