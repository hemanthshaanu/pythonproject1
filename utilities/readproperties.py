import configparser
config=configparser.RawConfigParser()
config.read("C:/Users/heman/PycharmProjects/pythonProject1/Configurations/config.ini")

class Readconfig():
    @staticmethod
    def getapplicationurl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info', 'user-email')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password