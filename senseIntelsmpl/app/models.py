"""
Definition of models.
"""
from django.db import models

# Create your models here.


class accel(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class accelRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class compassRaw(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

class gyro(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class gyroRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class orient(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class orientRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class SensorReading(models.Model):

    #Django creates a default id field with every model manual primary key creation is unnecessary 
            #sensorReadingID = models.AutoField(primary_key=True)
       
    humidity = models.IntegerField()
    temp = models.IntegerField()
    pressure = models.IntegerField()
    orient = orient
    orientRaw = orientRaw
    compass = models.IntegerField()
    compassRaw = compassRaw
    gyro =gyro
    gyroRaw = gyroRaw
    accel = accel
    accelRaw = accelRaw


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
