from django.db import models

class Parking_Lot(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=255)
    photo = models.CharField(default="files/pk_images/default.png",max_length=255)
    max_places = models.IntegerField(default=10)
    rating = models.FloatField(default=0)
    open_hour = models.IntegerField(default=7)
    close_hour = models.IntegerField(default=18)
    price = models.IntegerField(default=10)
    info = models.TextField(null=True,)
    lat = models.FloatField()
    longt = models.FloatField()

class User(models.Model):
    mat = models.CharField(primary_key=True,max_length=255,unique=True)
    password = models.CharField(max_length=255)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    parking_lot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)
    mat = models.ForeignKey(User,on_delete=models.CASCADE)
    penalty = models.IntegerField(default=0)
    date_time= models.DateTimeField(null=True)

class Rated(models.Model):
    id = models.AutoField(primary_key=True)
    parking_lot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)
    mat = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
