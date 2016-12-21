"""
Definition of models.
"""
from django.db import models

# Create your models here.
class Accel(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class AccelRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class CompassRaw(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

class Gyro(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class GyroRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class Orient(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class OrientRaw(models.Model):
    pitch = models.IntegerField()
    roll = models.IntegerField()
    yaw = models.IntegerField()

class SensorReading(models.Model):

    #Django creates a default id field with every model manual primary key creation is unnecessary 
            #sensorReadingID = models.AutoField(primary_key=True)
       
    humidity = models.IntegerField()
    temp = models.IntegerField()
    pressure = models.IntegerField()
    orient = models.ForeignKey(Orient)
    orientRaw = models.ForeignKey(OrientRaw)
    compass = models.IntegerField()
    compassRaw = models.ForeignKey(CompassRaw)
    gyro = models.ForeignKey(Gyro)
    gyroRaw = models.ForeignKey(GyroRaw)
    accel = models.ForeignKey(Accel)
    accelRaw = models.ForeignKey(AccelRaw)


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
    sensorReading = models.ForeignKey(SensorReading)
    gpsReading = models.ForeignKey(GpsReading)
