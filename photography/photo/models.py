from django.db import models

class Photos(models.Model):
    photo = models.ImageField()
    
