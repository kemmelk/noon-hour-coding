# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:55:08 2022

@author: KEmmelkamp
"""

import datetime as dt
import math

#Round hours
#The below functions round hours up

def RoundHoursUp(dateTime, roundValue):
    """Date utility function which rounds hours up to a set value of hour, 
       Preferably, a value which is a factor of 24, this function is not
       meant to be used by itself, but as a utility of other functions
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    :param roundValue: unsigned integer value which is a factor of 24 which 
                       which will be used to round up to
    :return RoundedTime: the original dateTime rounded up to the nearest six 
                         hours
    """
    
    time = dt.datetime.fromisoformat(dateTime)
    # The amount to add to original date time value
    hourMod = math.ceil(int(str(time.strftime("%H"))) / roundValue)
    
    RoundedTime = dt.datetime(time.year, time.month, time.day) \
        + dt.timedelta(hours=hourMod*roundValue)
    
    return RoundedTime

def RoundHoursUpTwo(dateTime):
    """Date utility function which rounds hours up to the next two hours, adds 
       a time delta if value is not already divisible by two hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest two 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 2)
        
    return RoundedTime

def RoundHoursUpThree(dateTime):
    """Date utility function which rounds hours up to the next three hours, adds 
       a time delta if value is not already divisible by three hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest three 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 3)
        
    return RoundedTime

def RoundHoursUpFour(dateTime):
    """Date utility function which rounds hours up to the next four hours, adds 
       a time delta if value is not already divisible by three hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest four 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 4)
        
    return RoundedTime

def RoundHoursUpSix(dateTime):
    """Date utility function which rounds hours up to the next six hours, adds 
       a time delta if value is not already divisible by six hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest six 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 6)
        
    return RoundedTime

def RoundHoursUpEight(dateTime):
    """Date utility function which rounds hours up to the next eight hours, adds 
       a time delta if value is not already divisible by three hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest eight 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 8)
        
    return RoundedTime

def RoundHoursUpTwelve(dateTime):
    """Date utility function which rounds hours up to the next twelve hours, 
       adds a time delta if value is not already divisible by three hours
    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded up to the nearest twelve 
                         hours
    """
    
    RoundedTime = RoundHoursUp(dateTime=dateTime, roundValue = 12)
        
    return RoundedTime
#The below functions round hours down

def RoundHoursDown(dateTime, roundValue):
    """Date utility function which rounds hours down to the previous time
       step divible by 6 hours, add the rounded hours to base date with a 
       timedelta

    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded down to the nearest six
                         hours
    """
    
    time = dt.datetime.fromisoformat(dateTime)
    # The amount to add to original date time value
    hourMod = math.floor(int(str(time.strftime("%H"))) / roundValue)
    
    RoundedTime = dt.datetime(time.year, time.month, time.day) \
        + dt.timedelta(hours=hourMod*roundValue)
        
    return RoundedTime
    
def RoundHoursDownSix(dateTime):
    """Date utility function which rounds hours down to the previous time
       step divible by 6 hours, add the rounded hours to base date with a 
       timedelta

    :param dateTime: datetime string written in iso format (YYYY-mm-dd hh:mm:ss)
    
    :return roundedtime: the original dateTime rounded down to the nearest six
                         hours
    """
    
    RoundedTime = RoundHoursDown(dateTime=dateTime, roundValue=6)
        
    return RoundedTime
    