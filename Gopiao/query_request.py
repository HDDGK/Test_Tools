import requests

from get_station import *
data=[]
type_data=[]
agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        ,'Cookie':'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-04-16&leftTicketDTO.from_station=TJP&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
         }
def query(data,from_station,go_station):
    data.clear()
    url="https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-04-16&leftTicketDTO.from_station=TJP&leftTicketDTO.to_station=BJP&purpose_codes=ADULT"
    response=requests.get(url,headers=headers)
    result=response.json()
    result=result['data']['result']
    if isStation()==True:
        station=eval(read())
        if len(result)!=0:
            for i in result:
                tmp_list=i.split('|')
                from_station=list(station.keys())[list(station.values()).index(tmp_list[6])]
                to_station=list(station.keys())[list(station.values()).index(tmp_list[7])]
                seat=[tmp_list[3],from_station,to_station,tmp_list[8],
                      tmp_list[9],tmp_list[10],tmp_list[32],tmp_list[31],
                      tmp_list[30],tmp_list[21],tmp_list[23],tmp_list[33],
                      tmp_list[28],tmp_list[24],tmp_list[29],tmp_list[26]]
                newSeat=[]
                for s in seat:
                    if s=="":
                        s="--"
                    else:
                        s=s
                    newSeat.append(s)
                data.append(newSeat)
        return data
def g_vehicle():
    if len(data)!=0:
        for g in data:
            i = g[0].startwith['G']
            if i:
                type_data.append(g)
def r_g_vehicle():
    if len(data)!=0:
        for g in data:
            i = g[0].startwith['G']
            if i:
                type_data.remove(g)
def d_vehicle():
    if len(data)!=0:
        for d in data:
            i = d[0].startwith['D']
            if i:
                type_data.append(d)
def r_d_vehicle():
    if len(data)!=0:
        for d in data:
            i = d[0].startwith['D']
            if i:
                type_data.remove(d)
def k_vehicle():
    if len(data)!=0:
        for k in data:
            i = k[0].startwith['D']
            if i:
                type_data.append(k)
def r_k_vehicle():
    if len(data)!=0:
        for k in data:
            i = k[0].startwith['D']
            if i:
                type_data.remove(k)
