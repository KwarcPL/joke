from django.db import models

# Create your models here.
class Joke(models.Model):
    joke_text = models.CharField('joke_text', max_length=1000)
    published_date = models.DateTimeField('date_published')
    accepted = models.BooleanField('accepted')
    rate = models.IntegerField('rate')
    number_of_grades = models.IntegerField('number_of_grades')
    tags = models.CharField('tags', max_length=100)


    class Meta:
        permissions = (("add_joke", "Can add joke"))
