import requests
import json


#from geolite2 import geolite2
#import geoip2.webservice


def convert_strDict(REQ):
    Dict = dict((x.strip(), y.strip())
         for x, y in (element.split('-')
            for element in REQ.split(', ')))
    return Dict


class Get_IP():
    def __init__(self):
        self.SELF_IP = requests.get('https://api.ipify.org').text  # api to pull self ip via text
       # self.write_wild = class_info.write_wild ## for extchanger.py

    def write_wild(self):
        pass

    @staticmethod
    def regex_inclusions(*args):
        pass

    def getParentDirectoryFromFile (self, absolutePathToFile):
        pass


    def Get_ip(self):
        global SELF_IP
        SELF_IP = requests.get('https://api.ipify.org').text  # api to pull self ip via text
        REQ00 = f"http://api.ipapi.com/{SELF_IP}?access_key=4c30512e8afe7d0a27c11e5deb4fce34"
        REQ = requests.get(REQ00).text
        res = json.loads(REQ), print(), print()
        print(SELF_IP)
        print('X' * 50)
        req_str = REQ.split(',', -1)
        print(req_str)
        print('X' * 50)
        print(type(req_str))
        ip = req_str[0]
        continent = req_str[3]
        country = req_str[5]
        state = req_str[7]
        city = req_str[8]
        zip = req_str[9]
        print(ip)
        print(continent)
        print(country)
        print(state)
        print(city)
        print(zip)
        print(), print(),
        print('X' * 50)

        return ip


get_info = Get_IP() ## XCLASS INSTANCE
######### TO RETURN WHOLE DICT ((( USE WHEN API IS FREE)) ###################
# IPA = get_info.Get_ip()
# IP = IPA
# print(IPA)
print('Famished')
## Use Get_IP if .API hits limit
#get_ip = get_info.Get_ip(SELF_IP)

get_ip = get_info.SELF_IP
print('X' * 50)
print('IP address :: ', get_ip)

#
#
