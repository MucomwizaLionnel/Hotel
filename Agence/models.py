from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 


class User(AbstractUser):
    is_Gerant=models.BooleanField(default='False')
    is_Caissier=models.BooleanField(default='False')
    is_Touriste=models.BooleanField(default='True')

class Gerant(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="gerant_user")


class Caissiere(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="caissiere_user")

class Touriste(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="touriste_user")