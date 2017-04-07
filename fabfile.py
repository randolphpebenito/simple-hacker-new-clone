from fabric.api import local

def deploy_to_heroku():
    local('./manage.py test topics')
    local('heroku maintenance:on')
    local('git push heroku master')
    local('heroku maintenance:off')

