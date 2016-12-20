"""
Definition of models.
"""
from django.db import models

# Create your models here.
class SensorReading(models.Model):

    #Django creates a default id field with every model manual primary key creation is unnecessary 
            #sensorReadingID = models.AutoField(primary_key=True)
       
    humidity = models.CharField(max_length = 50)
    temp = models.CharField(max_length = 50)
    pressure = models.CharField(max_length = 50)
    orient = models.CharField(max_length = 50)
    orientRaw = models.CharField(max_length = 50)
    compass = models.CharField(max_length = 50)
    compassRaw = models.CharField(max_length = 50)
    gyro = models.CharField(max_length = 50)
    gyroRaw = models.CharField(max_length = 50)
    accel = models.CharField(max_length = 50)
    accelRaw = models.CharField(max_length = 50)

class GpsReading(models.Model):

    latitude = models.IntegerField()
    longitude = models.IntegerField()
    timeUtc = models.TimeField()
    altitude = models.IntegerField()
    speed = models.IntegerField()
    climb = models.CharField(max_length = 50)

class Module(models.Model):

    moduleName = models.CharField(max_length = 50)
    ipAddress = models.GenericIPAddressField()

    SensorReading = SensorReading
    GpsReading = GpsReading 
