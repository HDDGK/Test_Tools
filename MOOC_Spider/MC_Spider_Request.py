import os.path

import requests

'''
方法
request:构造请求，支撑下方其他方法[]
requests.request(method=,url=,)
请求方式+url,自身可以实现下方的几种方式，下面是封装出来的方法

get:获取HTML网页,对应HTTP的get
head:获取HTML的头信息，对应HTTP的HEAD
poat:向HTML提交POSt请求，对应HTTP的POSt
put:向HTML提交的put请求，对应HTTP的put
patch:向HTML提交局部修改请求，对应HTTP的PATCH
delect:向HTML提交删除请求，对应HTTP的DELETE

参数
params：字典或者序列，作为参数加到url中

data：字典，序列，文件，作为request的内容，作为数据存储
json：JSON格式的数据，作为request的内容
header:字典，http的头字段{'user-agent':'chrome/10'}

cookies:字典，Cookie 、

jar，request的cookie
auth：HTTP认证功能
files：字典类型，传输文件
timeout：超时时间，以秒为单位
proxies：字典类型，设定代理服务器，增加登录认证

高级功能
allow_redirects：重定向
stream：获取内容立即下载
verify：认证ssl证书开关

cert：本地ssl证书路径



'''



def tryTry():
    r = requests.get("http://www.baidu.com")
    print(r.status_code)
    print(r.encoding)
    print(r.apparent_encoding)
    print(r.text)
    r.encoding = 'utf-8'
    print((r.text))


def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "程序异常"


def getJindong(url):
    try:
        r=requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        print(r.encoding)
        print(r.apparent_encoding)
        print(r.text[1000:2000])
    except:
        kv = {'user-agent': 'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        print(r.encoding)
        r.encoding='utf-8'
        print(r.text)
        print("爬取失败")


def keyword_request(url):
    keyword='Python'
    try:
        kv = {'wd':keyword}
        kv2 = {'user-agent': 'Mozilla/5.0'}
        print(url)
        r = requests.get(url, params=kv,headers=kv2)
        print(r.request.url)
        print(r.status_code)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("异常")


def picture_request():
    kv2 = {'user-agent': 'Mozilla/5.0'}
    url='https://lmg.jj20.com/up/allimg/tp09/210H51R3313N3-0-lp.jpg'
    path=r"C:\Users\HK145-TP\Desktop\新建文件夹\ABC.jpg"
    root=r"C:\Users\HK145-TP\Desktop\新建文件夹\\"
    autoPath=root+url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(autoPath):
            print(autoPath)
            r=requests.get(url,headers=kv2)
            print(r.status_code)
            with open(autoPath, 'wb') as f:
                f.write(r.content)  # r.content返回二进制形式
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


def find_ip_adress(url,kv):
    # pr={
    #     "http":
    #     "https":
    #     }
    r=requests.get((url+'202.204.80.112'),headers=kv)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    kv2 = {'user-agent': 'Mozilla/5.0'}
    url=["http://www.baidu.com",
         'https://item.jd.com/2967929.html',
         'https://www.amazon.cn/gp/product/B01M8L5Z3Y',
         'https://www.baidu.com/s',
         'https://m.ip138.com/ip.asp?ip=',
         'https://meeting.tencent.com/qrcode-login.html?redirect_link=https%3A%2F%2Fmeeting.tencent.com%2Fuser-center%2Fpersonal-information%3Freload%3D1&phone-number=',

         ]
    # print(getHtmlText(url[0]))
    # getJindong(url[1])
    # getJindong(url[2])
    # keyword_request(url[3])
    # picture_request()
    # find_ip_adress(url[4],kv2)