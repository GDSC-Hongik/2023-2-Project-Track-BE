from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length = 30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)