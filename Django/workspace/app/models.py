from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    passphrase = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
class Movies(models.Model):
    title = models.CharField(max_length=200)       # movie title
    description = models.TextField()               # longer text
    release_year = models.IntegerField()           # e.g. 2025
    duration = models.DurationField()              # e.g. 2h09m
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g. 7.5
    created_at = models.DateTimeField(auto_now_add=True)  # auto add timestamp

    def __str__(self):
        return self.title