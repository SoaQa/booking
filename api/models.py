from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Hotel(models.Model):
    name = models.CharField(max_length=128)


class Room(models.Model):
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='bookings', on_delete=models.CASCADE)
