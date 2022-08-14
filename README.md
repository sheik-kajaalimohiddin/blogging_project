# blogging_project
#####################################
Pre-requisties
#####################################
1. Python need to be installed 
Python version -  3.8.6

2. pip to installed


2.IDE used - PyCharm 2020.3.1 (Community Edition)

3. installed django framework
pip install django

to check version of the django

py -m django --version or django-admin --version

How to create project in django

django-admin startproject <project_name>

project_name/
   manage.py
   project_name/
      __init__.py
      settings.py
      urls.py
      wsgi.py

How to create application in django

django-admin startapp <application_name>


To run webserver

python manage.py runserver

##########################################
Project description
##########################################

This project objective is to post questions by the users who are logged/register into the website.

Features:
Users can register to the website
Users can login,logout,view their profile,post their queries once they login into the system
They can reset their password using email verification link.

#########################################
deployment details
#########################################
This application is deployed on Heroku webserver provide which can be accessed from any where in the world by url provided by it
#############
pre-requistes
#############
Need login details of Heroku application

Need to initiate current working directory into git repository

install gunicorn
pip isntall gunicorn

Heroku create <webapplicaiton_name> - url used to open the application deployed in heroku

Requirements.txt - contains what are applications/software to be installed for the application successful run(They can be taken from pip freeze command)

Procfile - no extension to be given. This file contains web:gunicorn <Project_name>.wsgi this avoids no web process error

update settings.py file with <url> in allowed hosts section

import django_heroku and add django_heroku.settings(locals()) - to get database access by heroku which it will be taking care

if any database changes are done run

Heroku run python manage.py migrate

to open application

Heroku open

If there are any changes done in application, do run git commands and run below commands to apply changes done

git add -A

git commit -m "commit message"

git push heroku master

heroku open

Then application will be opened in the browser with https://<webapplication_name>.herokuapp.com

