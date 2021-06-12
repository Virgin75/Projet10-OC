# Django API for issue tracking
Project 10 - Openclassrooms

> The API documentation is available on this page : https://documenter.getpostman.com/view/11214441/TzXwEyJM

## Description
This is a CRUD API developped with Python's web development framework Django.
It is meant to help developers track issues in their software. Each issue is related to a specific project. All the endpoints are protected. You need to be logged in (with JWT) to access them. Some route need object level permissions in order to be accessed. 

Please find below the available models and their relations.
![alt text](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python+FR/P8+-+Cr%C3%A9ez+une+API+s%C3%A9curis%C3%A9e+RESTful+en+utilisant+Django+REST+/Class+Diagram+for+P8.png)

## Installation
Here's how to start the development server:

1. Clone this repo and 'cd' to the local directory.
2. Create a new virtual environement with '''console python3 -m venv env'''
3. Activate this virtual env with '''console source env/bin/activate'''
4. Install the required dependencies with '''console pip3 install -r requirements.txt'''
5. Start the server with '''console python3 manage.py runserver'''
