from turtle import mode
from django.db import models

# Create your models here.

class ImageModel(models.Model):
    images = models.ImageField(upload_to="photos/%Y/%m/%d/")
    heading = models.CharField(max_length=30)
    sub_heading = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.heading