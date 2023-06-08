import requests
import traceback
import re
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        kv={'user-agent': 'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)
        return r.text
    except:
        print("网页信息获取报错")
def getStockList(lst,stockURL):
    html=getHtmlText(stockURL)
    soup=BeautifulSoup(html,'html.parser')
    # print(soup.body.contents)
    tr=soup.find_all('div' ,class_="listview full")
    print("?")

    print(tr)

    print("?")
    '''
    嵌套查找
        xx={}
        soup=BeautifulSoup(html,'html.parser')
        info=sopu.find('div',attrs{'class':'xxxx'})
        bb_info=info.find('div',attrs{'class':'xxxx'})[x]
        xx.updata({'xxxx':bb_info.text.split()[0]})
    一步步赛选出来有用信息
    '''

    '''
    print("XXX")
    print(tr)
    for i in tr:
        try:
            a=soup.find_all('a')
            # print(a)


        #     href=i.attrs['href']
        #     # lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        #     lst.append(re.findall(r'\d{6}',href)[0])
        except:
            continue
    # print(lst)
    '''

def getStockInfo(lst,stockURL,fpath):
    return ""


def main():
    # stck_list_url="http://quote.eastmoney.com/stocklist.html"
    # stck_list_url="http://quote.eastmoney.com/center/gridlist.html#hs_a_board"
    stck_list_url="http://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124015222800625985577_1685543711078&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1685543711079"
    stck_info_url="http://gupiao.baidu.com/stock/"
    output_file=r"C:\Users\HK145-TP\Desktop\新建文件夹\BaiduStockList.txt"
    slist=[]
    getStockList(slist,stck_list_url)
    getStockInfo(slist,stck_info_url,output_file)
if __name__ == '__main__':

    main()