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

def getRootDirectory():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['rootDirectory']

def getRegisterKey():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['registerKey']

def getWorksheetPush():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['worksheetPush']

def getWorksheetPull():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['worksheetPull']

def doWorksheetPush():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['pushToWorksheet']

def doSetLikelyPassword():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['setLikelyPassword']

def getLikelyPassword():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['likelyPassword']

def getUnlikelyPassword():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    return Config['Individual']['unlikelyPassword']

def setDoSetLikelyPassword(doSetLikelyPassword):
    if(doSetLikelyPassword == ""):
        return

    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['setLikelyPassword'] = doSetLikelyPassword

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setLikelyPassword(likelyPassword):
    if(likelyPassword == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['likelyPassword'] = likelyPassword

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setUnlikelyPassword(unlikelyPassword):
    if(unlikelyPassword == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['unlikelyPassword'] = unlikelyPassword

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setWorksheetPush(worksheetPush):
    if(worksheetPush == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['worksheetPush'] = worksheetPush

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setWorksheetPull(worksheetPull):
    if(worksheetPull == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['worksheetPull'] = worksheetPull

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setDoWorksheetPush(doWorksheetPush):
    if(doWorksheetPush == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['pushToWorksheet'] = doWorksheetPush

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setRegisterKey(registerKey):
    if(registerKey == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['registerKey'] = registerKey

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setRootDirectory(rootDirectory):
    if(rootDirectory == ""):
        return
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    Config['Individual']['rootDirectory'] = rootDirectory

    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setServiceAccount(ServiceKey):
    if(ServiceKey == ""):
        return
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['ServiceKey'] = ServiceKey
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setSheetKey(SheetKey):
    if(SheetKey == ""):
        return
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['SheetKey'] = SheetKey
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setSheetName(SheetName):
    if(SheetName == ""):
        return
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Individual']['SheetName'] = SheetName
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()

def setTimingMultiplier(TimingMultiplier):
    if(TimingMultiplier == ""):
        return
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    Config['Additional']['TimingMultiplier'] = TimingMultiplier
    
    with open('config.ini', 'w+') as configfile:
        Config.write(configfile)
        configfile.close()
