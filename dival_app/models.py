from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=6)
    Email = models.EmailField(max_length=256)
    address = models.CharField(max_length=345,blank=True)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.username
