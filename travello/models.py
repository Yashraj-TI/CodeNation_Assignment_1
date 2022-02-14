from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from sre_parse import CATEGORIES
from tkinter import CASCADE
from django.db import models
from datetime import date, datetime

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=100)
    Num_of_Buisness = models.IntegerField(default=1)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

class Restaurant(models.Model):
    Name  = models.CharField(max_length=100)
    Neighbourhood = models.CharField(max_length=200)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    IsOpen = models.BooleanField(default=False)
    Category = models.CharField(max_length=100)
    Stars = models.IntegerField(default=1)
    ReviewCount = models.IntegerField(default=1)

class Review(models.Model):
    Restaurant_Id = models.IntegerField()
    Stars = models.IntegerField(default=1)
    Date = models.DateField(default = datetime.now, editable=False)
    Text = models.TextField()

