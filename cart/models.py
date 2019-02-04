from django.contrib.auth.models import User
from django.db import models
from buyer.models import Buyer
from photographer.models import Photographer, Photo


class Cart(models.Model):
	buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
	payment_status = models.CharField(max_length=1, choices= (('S', 'Success'),('F', 'Failed'),('P', 'Pending')))

class CartItem(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)