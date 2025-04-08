from django.db import models

class Photos(models.Model):
    CATEGORY_CHOICES = [
        ('portrait', 'Portrait'),
        ('wedding', 'Wedding'),
        ('nature', 'Nature'),
        ('street', 'Street'),
        ('document', 'Documentary')
    ]
    
    photo = models.ImageField(null=True, upload_to='images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='portrait')
    title = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.category} - {self.title if self.title else 'Untitled'}"
