import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def getUserMobileNumber():
        mobilenumber = config.get('common info', 'mobilenumber')
        return mobilenumber
    
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
    
    @staticmethod
    def getvehicleName():
        vehicleName = config.get('common info', 'vehicleName')
        return vehicleName
    
    @staticmethod
    def getpartName():
        partName = config.get('common info', 'partName')
        return partName
    
    @staticmethod
    def getFirstPartSearch():
        firstpartsearch = config.get('common info', 'firstpartsearch')
        return firstpartsearch
    
    @staticmethod
    def getSecondPartSearch():
        secondpartsearch = config.get('common info', 'secondpartsearch')
        return secondpartsearch
    

    @staticmethod
    def getBulkUploadFile():
        bulkuploadfile = config.get('common info', 'bulkuploadfile')
        return bulkuploadfile