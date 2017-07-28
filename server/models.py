from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class ConvenienceReservation:
    hash_num = models.CharField(primary_key=True, max_length=7)
    
    sender_name = models.CharField(max_length=6)
    sender_phone = models.CharField(max_length=13)
    sender_addr = models.CharField(max_length=60)
    
    receiver_name = models.CharField(max_lengh=6)
    receiver_phone = models.CharField(max_length=13)
    receiver_addr = models.CharField(max_length=60)
    
    stuff_weight = models.IntegerField()
    stuff_caution = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.hash_num


class UserInfo:
    name = models.CharField(max_length=6)
    phone = models.CharField(max_length=13)
    addr = models.CharField(primary_key=True, max_length=60)
    kakao_id = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.kakao_id


class ShopInfo:
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return self._id

    def latitude(self):
        return self.location.y

    def longitude(self):
        return self.location.x
