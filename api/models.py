from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Hotel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Room(models.Model):
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.name}. Room num: {self.num}"


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='bookings', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}; {self.room.hotel.name}; {self.room.num}"
