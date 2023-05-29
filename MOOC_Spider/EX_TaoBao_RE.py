import requests
import re

def getHtmlText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)
        if len(r.text)>100:
            print("网页获取成功")
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        print(plt)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            print(price)
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
            printGoodsList(ilt)
    except:
        return ""


def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHtmlText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

if __name__ == '__main__':
    main()