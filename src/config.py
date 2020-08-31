import configparser
import io
import os

##[Individual]
##ServiceKey: NULL
##SheetKey: NULL
##SheetName: NULL

##[Additional]
##TimingMultiplier: 1

def getServiceAccount():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['ServiceKey']

def getSheetKey():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['SheetKey']

def getSheetName():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['SheetName']

def getTimingMultiplier():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Additional']['TimingMultiplier']

def setServiceAccount(ServiceKey):
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['ServiceKey'] = ServiceKey
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)

def setSheetKey(SheetKey):
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['SheetKey'] = SheetKey
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)

def setSheetName(SheetName):
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['SheetName'] = SheetName
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)

def setTimingMultiplier(TimingMultiplier):
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Additional']['TimingMultiplier'] = TimingMultiplier
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)

setServiceAccount("Testing")
setTimingMultiplier("2")
setSheetKey("test")
setSheetName("Garrett")