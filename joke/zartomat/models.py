from django.db import models

# Create your models here.
class Joke(models.Model):
    joke_text = models.CharField('joke_text', max_length=200)
    published_date = models.DateTimeField('date published')
    accepted = models.BooleanField('accepted')
    rate = models.IntegerField('rate')
    number_of_grades = models.IntegerField('number_of_grades')
