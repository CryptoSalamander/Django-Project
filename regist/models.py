from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    person_number = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    account = models.CharField(max_length=75)
    account_pw = models.CharField(max_length=50)
    hellonumber = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
