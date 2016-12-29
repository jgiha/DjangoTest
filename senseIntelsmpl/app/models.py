"""
Definition of models.
"""
from django.db import models
from django.contrib.postgres.fields import JSONField


#!flask/bin/python
from flask import Flask, jsonify, make_response
from collections import defaultdict
from sense_hat import SenseHat

import time
import os
from gpsd import *
from time import *
import threading


class SensorReading(models.Model):
    humidity = []
    temp = []
    pressure = []
    orient = []
    orientRaw = []
    compass = []
    compassRaw = []
    gyro = []
    gyroRaw = []
    accel = []
    accelRaw = []
    sensorList = defaultdict(list)
    sensorList["humidity"] = humidity
    sensorList["temp"] = temp
    sensorList["pressure"] = pressure
    sensorList["orient"] = orient
    sensorList["orientRaw"] = orientRaw
    sensorList["compass"] = compass
    sensorList["compassRaw"] = compassRaw
    sensorList["gyro"] = gyro
    sensorList["gyroRaw"] = gyroRaw
    sensorList["accel"] = accel
    sensorList["accelRaw"] = accelRaw
    
    sense = SenseHat()

    def add(x,y): return x+y

    def __str__(self): 
        return self.sense

    @classmethod
    def get_sensorReadings():
        sensor = [
            {
                'humidity': sense.humidity,
                'temp': sense.temp,
                'pressure': sense.pressure,
                'orient': sense.orientation,
                'orientRaw': sense.orientation_radians,
                'compass': sense.compass,
                'compassRaw': sense.compass_raw,
                'gyro': sense.gyro,
                'gyroRaw': sense.gyro_raw,
                'accel': sense.accel,
                'accelRaw': sense.accel_raw
            }
        ]
        return jsonify({'sensor': sensor})

    @classmethod
    def getSingleSensorReading(cls,*args,**kwargs):
        #sensorReadings 
        cls.sensorList['humidity'].append(sense.humidity)
        cls.sensorList['accel'].append(sense.accel)
        cls.sensorList['temp'].append(sense.temp)
        cls.sensorList['pressure'].append(sense.pressure)
        cls.sensorList['orient'].append(sense.orientation)
        cls.sensorList['orientRaw'].append(sense.orientation_radians)
        cls.sensorList['compass'].append(sense.compass)
        cls.sensorList['compassRaw'].append(sense.compass_raw)
        cls.sensorList['gyro'].append(sense.gyro)
        cls.sensorList['gyroRaw'].append(sense.gyro_raw)
        cls.sensorList['accelRaw'].append(sense.accel_raw)
        return cls.sensorList

    @classmethod
    def get_sensorReadingsAvg(cls,times):

        finalSensorData = {}
        for _ in xrange(int(times)):
            sensorList = getSingleSensorReading(cls.sensorList)
            time.sleep(1)
        #sum(int(i) for i in data) 
        finalSensorData['humidity'] = sum(cls.sensorList['humidity'])/len(cls.sensorList['humidity'])
        finalSensorData['temp'] = sum(cls.sensorList['temp'])/len(cls.sensorList['temp'])
        finalSensorData['pressure'] = sum(cls.sensorList['pressure'])/len(cls.sensorList['pressure'])
        returnData = {'avgs': jsonify(finalSensorData), 'raw': jsonify(cls.sensorList)}
        print (cls.sensorList)
   
        return cls.sensorList


class GpsReading(models.Model, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    name = models.CharField(max_length = 250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timeUtc = models.TimeField()
    altitude = models.IntegerField()
    speed = models.IntegerField()
    climb = models.CharField(max_length = 250)

    def __str__(self): 
        return self.name

    @classmethod
    def get_gpsReadings():
        global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
    def run(self):
      global gpsd
      while gpsp.running:
        gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
    if __name__ == '__main__':
      gpsp = GpsPoller() # create the thread

    try:
        gpsp.start() # start it up
        while True:
              gps = [{
                      'latitude': gpsd.fix.latitude,                          
                      'longitude': gpsd.fix.longitude,                                   
                      'timeUtc':gpsd.utc + '+' + gpsd.fix.time,                
                      'altitude':gpsd.fix.altitude,                           
                      'speed': gpsd.fix.speed,
                      'climb':  gpsd.fix.climb
                  }]
              jsonify({'gps': gps})

              time.sleep(1) #set to whatever
 
    except(KeyboardInterrupt, SystemExit): #when you press ctrl+c
     print ("\nKilling Thread...")
     gpsp.running = False
     gpsp.join() # wait for the thread to finish what it's doing
    print ("Done.\nExiting.")

class Module(models.Model):

    moduleName = models.CharField(max_length = 250)
    ipAddress = models.GenericIPAddressField()
    sensorData = JSONField()
    sensorReadingAvg = JSONField()
    gpsData = JSONField()

    def __str__(self): 
        return self.moduleName
   
    #gpsReading = models.ForeignKey(GpsReading)
    #sensorReading = models.ForeignKey(SensorReading)
    







#sched = Scheduler()
#sched.start()

#def some_job():
    #print "Every 10 seconds"

#sched.add_interval_job(some_job, seconds = 1)

#sched.shutdown()
#@app.route('/')
#def index():
#    return "Hello World"


#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify({'error': 'Not data found on sensor'}), 404)

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)




## Create your models here.
#class Accel(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class AccelRaw(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class CompassRaw(models.Model):
#    x = models.IntegerField()
#    y = models.IntegerField()
#    z = models.IntegerField()

#class Gyro(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class GyroRaw(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class Orient(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class OrientRaw(models.Model):
#    pitch = models.IntegerField()
#    roll = models.IntegerField()
#    yaw = models.IntegerField()

#class SensorReading(models.Model):

#    #Django creates a default id field with every model manual primary key creation is unnecessary 
#            #sensorReadingID = models.AutoField(primary_key=True)
     
#    humidity = models.IntegerField()
#    temp = models.IntegerField()
#    pressure = models.IntegerField()
#    orient =  models.ForeignKey(Orient, on_delete=models.CASCADE)
#    orientRaw = models.ForeignKey(OrientRaw, on_delete=models.CASCADE)
#    compass = models.IntegerField()
#    compassRaw = models.ForeignKey(CompassRaw, on_delete=models.CASCADE)
#    gyro =  models.ForeignKey(Gyro, on_delete=models.CASCADE)
#    gyroRaw = models.ForeignKey(GyroRaw, on_delete=models.CASCADE)
#    accel = models.ForeignKey(Accel, on_delete=models.CASCADE)
#    accelRaw = models.ForeignKey(AccelRaw, on_delete=models.CASCADE)

















#class GpsPoller(threading.Thread):
#  def __init__(self):
#    threading.Thread.__init__(self)
#    global gpsd #bring it in scope
#    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
#    self.current_value = None
#    self.running = True #setting the thread running to true
 
#  def run(self):
#    global gpsd
#    while gpsp.running:
#      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
#if __name__ == '__main__':
#  gpsp = GpsPoller() # create the thread
#  try:
#    gpsp.start() # start it up
#    while True:
#      #It may take a second or two to get good data
#      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
#      #os.system('clear')
 
#      #print
#      print (' GPS reading')
#      print ('----------------------------------------')
#      print ('latitude    ' , gpsd.fix.latitude             )   
#      print ('longitude   ' , gpsd.fix.longitude            )
#      print ('time utc    ' , gpsd.utc,' + ', gpsd.fix.time )
#      print ('altitude (m)' , gpsd.fix.altitude             )
#      #print( 'eps         ' , gpsd.fix.eps                 )
#      #print( 'epx         ' , gpsd.fix.epx                 )
#      #print( 'epv         ' , gpsd.fix.epv                 )
#      #print( 'ept         ' , gpsd.fix.ept                 )
#      print ('speed (m/s) ' , gpsd.fix.speed                )
#      print ('climb       ' , gpsd.fix.climb                )
#      #print( 'track       ' , gpsd.fix.track               )
#      #print( 'mode        ' , gpsd.fix.mode                )
#      #print(                                               )
#      #print( 'sats        ' , gpsd.satellites              )
 
#      time.sleep(1) #set to whatever
 
#  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
#    print ("\nKilling Thread...")
#    gpsp.running = False
#    gpsp.join() # wait for the thread to finish what it's doing
#  print ("Done.\nExiting.")

##sense = SenseHat()

##def add(x,y): return x+y