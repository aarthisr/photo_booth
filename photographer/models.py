from django.contrib.auth.models import User
from django.db import models


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices= (('M', 'Male'),('F', 'Female')))
    mobile_no = models.IntegerField()
    photographer_photo = models.ImageField(blank=True)
    paypal_id = models.TextField()
    category = models.TextField()
    experience = models.FloatField()
    description = models.TextField()
    availibility = models.TextField()
    date = models.DateField(auto_now_add=True, auto_now=False)



class Photo(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    url = models.TextField()
    date = models.DateField(auto_now_add=True, auto_now=False)
    price = models.FloatField()
    title = models.TextField()
    category = models.TextField()
    description = models.TextField()
    likes = models.IntegerField()
    thumbnail_path = models.TextField()


class Photo_rating(models.Model):
    phot_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    like = models.IntegerField()
    dislike = models.IntegerField()
    count_sold = models.IntegerField()
