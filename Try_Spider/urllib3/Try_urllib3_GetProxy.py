import requests
from lxml import etree
import pandas as panda

url_Proxy="https://www.xicidaili.com/nn/"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
response=requests.get(url=url_Proxy,headers=headers)
response.encoding='utf-8'
if response.status_code==200:
    html=etree.HTML(response.text)
    table=html.xpath('//table[@id="ip_list"]')[0]
    trs=table.xpath('//tr')[1:]
    ip_table=panda.DataFrame(columns=['ip'])
    ip_list=[]
    for t in trs:
        ip =t.xpath('td/text()')[0]
        port=t.xpath('td/text()')[1]
        ip_list.append(ip+'port')
        print('代理IP为：',ip,'，对应端口为：',port)
    ip_table[ip]=ip_list
    ip_table.to_excel('ip.xlsx',sheet_name='data')


