from django.db import models

# Create your models here.
class Joke(models.Model):
    joke_text = models.CharField('joke_text', max_length=200)
    published_date = models.DateTimeField('date_published')
    accepted = models.BooleanField('accepted')
    rate = models.IntegerField('rate')
    number_of_grades = models.IntegerField('number_of_grades')

class User(models.Model):
    login = models.CharField('login', max_length=50)
    password = models.CharField('password', max_length=50)
    email = models.EmailField('email')
    registration_date = models.DateTimeField('registration_date')
    banned = models.BooleanField('banned')
    mod = models.BooleanField('mod')

