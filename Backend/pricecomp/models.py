# models.py

# from django.db import models
from djongo import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()
    rank = models.IntegerField()
    is_metro_city = models.BooleanField(default=False)
    is_tourist_destination = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    hotel_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    description = models.TextField()
    # rating = models.DecimalField(max_digits=3, decimal_places=1)
    # amenities = models.TextField()  # You might want to consider a better way to store amenities
    star_rating = models.DecimalField(max_digits=10, decimal_places=2)
    airport_dist = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=20)
    free_wifi = models.BooleanField(default=False)
    free_breakfast = models.BooleanField(default=False)
    hotel_capacity = models.IntegerField(default=0)
    has_swimming_pool = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You should handle password hashing

    def __str__(self):
        return self.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"
class Pricing(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_weekend = models.BooleanField(default=False)
    is_new_year_eve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type} - {self.date}"