import requests
import re
import os
def getStation():
    url_station_Name="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9259"
    response=requests.get(url_station_Name,verify=True)
    staion_name=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
    staion_name=dict(staion_name)
    staion_name=str(staion_name)
    write(staion_name)

def write(stations):
    file=open("station.text",'w',encoding='utf_8')
    file.write(stations)
    file.close()
def read():
    file=open("station.text",'r',encoding='utf_8')
    data=file.readline()
    file.close()
    return data
def isStation():
    isStation=os.path.exists('station.text')
    return isStation