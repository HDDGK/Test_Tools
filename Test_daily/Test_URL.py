import urllib.parse
import urllib.request
import urllib3
print(r"安装位置c:\users\hk145-tp\appdata\local\programs\python\python311\lib\site-packages (1.26.15)")
# response=urllib.request.urlopen('http://www.baidu.com')
# html=response.read()
#
# data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# html=response.read()
# print(html)
#
# http=urllib3.PoolManager()
# response2=http.request('GET','http://www.baidu.com')
# print(response2.data)
#
# response2=http.request('POST','http://httpbin.org/post',fields={'world':'hello'})

# import requests
# print(r"安装位置 c:\users\hk145-tp\appdata\local\programs\python\python311\lib\site-packages (from requests) (3.1.0)")
# resp=requests.get('http://www.baidu.com')
# print(resp.status_code,"\nstatus_code\n")
# print(resp.url,"\nurl\n")
# print(resp.headers,"\nheaders\n")
# print(resp.cookies,"\ncookies\n")
# print(resp.text,"\ntext\n")
# print(resp.content,"\ncontent\n")

import requests
data1={'word':'hello'}
resp2=requests.post('https://httpbin.org/post',data=data1)
print(resp2.content)
print("注意这里的https和http有区别")

# requests.put('https://httpbin.org/post',data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.options('https://httpbin.org/get')

url_name='http://www.baidu.com'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36)Gecko/20100101 Firefox/59.0'}
resp4=requests.get(url_name,headers=headers)
print(resp4.content)

for a in range(0,100):
    try:
        resp5=requests.get(url_name,timeout=0.05)
        print(resp5.status_code)
    except Exception as e:
        print("异常"+str(e))
# proxy={'http':'http://http://150.138.253.72.808','https':'https://https://150.138.253.72.808'}
# resp6=requests.get(url_name,proxies=proxy)
# print(resp6.content)
print("代理访问失败")

from bs4 import BeautifulSoup
html_doc="""
<html>
<head><title>???</title></head>
<body>
<a href="http://example.com/else" class="sister" id="link1">elsie</a>
</body>
</html>
"""
soup=BeautifulSoup(html_doc,features="lxml")
print(soup)