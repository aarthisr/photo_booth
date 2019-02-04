from django.contrib.auth.models import User
from django.db import models


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices= (('M', 'Male'),('F', 'Female')))
    user_photo = models.ImageField(blank=True)
    mobile_no = models.IntegerField()
