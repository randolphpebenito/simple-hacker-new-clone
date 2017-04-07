# Overview

A simple Digg/Reddit Clone Django app with upvote/downvote functionality using jQuery and Aja. 
It can easily be deployed to Heroku.

Detailed steps on how to run/deploy [Django Reddit/Digg Clone Simple](https://docs.google.com/document/d/1D9ghvQvaLUNOf4zczapshSHXk3DaSyiEid555pgQtDA/edit#heading=h.55eevtewll6k).

## Demo
Heroku: https://randolph-caroureddig-clone.herokuapp.com/   
Python Anywhere: http://randolphcaroucodingexer.pythonanywhere.com/
## Quickstart

### Running Locally

```sh
$ git clone https://github.com/randolphpebenito/simple-hacker-new-clone.git
$ cd simple-hacker-new-clone
$ virtualenv <venv name>
$ source <venv name>/bin/activate
$ pip install -r requirements.txt
$ ./manage.py test topics #Run the tests
$ ./manage.py collectstatic

Via Heroku
$ heroku local

Via Django’s built in web server
$ ./manage.py runserver
```

Your app should now be running on [localhost:5000](http://localhost:5000/). or [localhost:8000](http://localhost:8000/)

### Deploying to Heroku

```sh
$ heroku create #Run this if first time to deploy
$ fab deploy_to_heroku
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Deploying to Python Anywhere

See step-by-step guide on how to deply your Django project to Python Heroku via Django Girls tutorial:

- [Deploy Django on Python Anywhere](https://tutorial.djangogirls.org/en/deploy/#setting-up-our-blog-on-pythonanywhere)
