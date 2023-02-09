from django.db import models

# Create your models here.
class Pet (models.Model):

    SEX_CHOICES = [ ( 'M', 'Male' ), ( 'F', 'Female' ), ( 'O', 'Others' ) ]

    name = models.CharField(max_length=100)
    submitter = models.CharField (max_length=100)
    submission_date = models.DateTimeField(auto_now=True)
    description = models.TextField (max_length=1000)
    breed = models.CharField (max_length= 100)
    species = models.CharField (max_length=100)
    sex = models.CharField (choices=SEX_CHOICES, blank=True, max_length=50)
    age = models.IntegerField (null = True)
    vaccinations = models.ManyToManyField ('Vaccine', blank=True)

class Vaccine (models.Model): 
    name = models.CharField (max_length=1000)

    def __str__ (self):
        return self.name

class Person (models.Model):
    name = models.CharField (max_length=100)
    age = models.IntegerField(null=False)