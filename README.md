# HelpDesk
It's a online ticketing system where user can create a ticket for help and track the update. This project is running on django version 4.2.7 and python version 3.10.12


# Introduction
The goal of this project is to learn django professional and everyone can use this project. 

_Also_ want to cover up this things

* User Authentication and Authorization
* 2FA integration
* Templates and Static Files
* Models and Database Interactions
* MySQL Database Configuration
* Deployment
* Logging and Monitoring
* Documentation
* Version Control and Collaboration


# Project Setup

To use this project to your own machine follow this steps

### Clone repository from github

First of all, clone this repository using this command

    git clone https://github.com/mehedishovon01/HelpDesk.git

### Create a virtualenv

Make a virtual environment to your project directory. Let's do this,

If you have already an existing python3 virtualenv then run this

    virtualenv venv

Or if virtualenv is not install in you machine then run this

    python3 -m venv venv
    
Activate the virtual environment and verify it

    . venv/bin/activate

### Install the dependencies

Most of the projects have dependency name like requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file.

    pip install -r requirements.txt

### Create database

We have already sqlite3 setup in our project.

So, simply apply the migrations:

    python3 manage.py migrate
    
Boooooom! Your project setup is done.

### Run this project

Let's run the development server:

    python3 manage.py runserver

That’s it! Now you’re project is already run into a development server. 

Just click this link, [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


# Database Configuration

I am using `MySQL` database here. To configure MySQL in your Django project, you'll need to update the `DATABASES` setting in your settings.py file as follows:

    'default': {  
    'ENGINE': 'django.db.backends.mysql',  
    'NAME': 'database_name',
    'USER': 'root',  
    'PASSWORD': 'mysql_password',  
    'HOST': '127.0.0.1',  
    'PORT': '3306',  
    'OPTIONS': {  
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }
    }


[See User](user/readme.md)


Thanks for reading.