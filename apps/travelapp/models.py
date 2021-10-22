from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatar')
    bio = models.TextField()

    def __str__(self):
        return self.name