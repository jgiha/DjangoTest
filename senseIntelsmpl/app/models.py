"""
Definition of models.
"""
from django.db import models

# Create your models here.


class accel(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class accelRaw(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class compassRaw(models.Model):
    x = models.DecimalField(max_digits = 50)
    y = models.DecimalField(max_digits = 50)
    z = models.DecimalField(max_digits = 50)

class gyro(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class gyroRaw(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class orient(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class orientRaw(models.Model):
    pitch = models.DecimalField(max_digits = 50)
    roll = models.DecimalField(max_digits = 50)
    yaw = models.DecimalField(max_digits = 50)

class SensorReading(models.Model):

    #Django creates a default id field with every model manual primary key creation is unnecessary 
            #sensorReadingID = models.AutoField(primary_key=True)
       
    humidity = models.DecimalField(max_digits = 50)
    temp = models.DecimalField(max_digits = 50)
    pressure = models.DecimalField(max_digits = 50)
    orient = orient
    orientRaw = orientRaw
    compass = models.DecimalField(max_digits = 50)
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
