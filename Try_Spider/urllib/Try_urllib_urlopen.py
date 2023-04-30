import socket
import urllib.request
import urllib.parse
import urllib.error
url='https://www.baidu.com/'
url2='https://www.httpbin.org/post'
url3='https://www.httpbin.org/'
url4='http://site2.rjkflm.com:666/index/index/chklogin.html'
url5='https://www.httpbin.org/post'
url6='http://site2.rjkflm.com:666/123index.html'
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36)Gecko/20100101 Firefox/59.0'}

String_Chooice = ['[1]GET请求',
                  '[2]POST请求',
                  '[3]网络超时',
                  '[4]完整网络请求',
                  '[5]GET请求',
                  '[6]Cookies',
                  '[7]代理IP',
                  '[8]异常处理',
                  ]
def function8():
      try:
            parse_result=urllib.parse.urlparse(url4)
            print(type(parse_result))
            print(parse_result)
            print("8")
            response=urllib.request.urlopen(url6)
      except urllib.error.HTTPError as error2:
            print("HTTP")
            print(error2.reason)
            print(error2.code)
            print(error2.headers)
      except urllib.error.URLError as error:
            print(error.reason)


def function7():
      proxy_handler=urllib.request.ProxyHandler({
            'http':'58.220.95.114.10053'
      })
      opener=urllib.request.build_opener(proxy_handler)
      response=opener.open(url,timeout=2)
      print(response.read().decode('utf-8'))
      print("这里http不同，结果可能报错，而且HTTP和https也是不同，他妈的书上也不说，是个会写书的")

def function6():
      url="http://site2.rjkflm.com:666/index/index/chklogin.html"
      data=bytes(urllib.parse.urlencode({'username':'mrsoft','password':'mrsoft'}),encoding='utf-8')
      r=urllib.request.Request(url=url4,data=data,method='POST')
      response=urllib.request.urlopen(r)
      print(response.read().decode('utf-8'))

def function5():
      r=urllib.request.Request(url=url,headers=headers)
      response=urllib.request.urlopen(r)
      print(response.read().decode('utf-8'))

def function4():
      data=bytes(urllib.parse.urlencode({'hello':'Python'}),encoding='utf-8')
      r=urllib.request.Request(url=url2,data=data,headers=headers,method='POST')
      response=urllib.request.urlopen(r)
      print("注意类型错误：urlopen（）缺少1个必需的位置参数：“url”","TypeError: urlopen() missing 1 required positional argument: 'url'")
      print(response.read().decode('utf-8'))
def function3():
      try:
            response=urllib.request.urlopen(url=url3,timeout=0.1)
            print(response.read().decode('utf-8'))
            #设置网络超时阈值，0.1高门槛
      except urllib.error.URLError as error:
            if isinstance(error.reason,socket.timeout):
                  print('任务超时，执行下一个任务')

def function2():
      data=bytes(urllib.parse.urlencode({'helo':'Python'}),encoding='utf-8')
      print("注意：encoding 和 encodings 的区别")
      response=urllib.request.urlopen(url=url2,data=data)
      print(response.read().decode('utf-8'))

def function1():
      print("Function1")
      reponse = urllib.request.urlopen(url=url)
      print('响应数据类型为：', reponse.status)

      print('响应头所有信息', reponse.getheaders())
      print('响应头指定信息', reponse.getheader('Accept-Ranges'))
      print("\n需注意，这里getheader方法和getheaders参数是不同的\n",
            "TypeError: HTTPResponse.getheaders() takes 1 positional argument but 2 were given\n")

      print('Python 官网HTML代码如下', reponse.read().decode('utf-8'))

if __name__=='__main__':
      for i in String_Chooice:
            print(i)
      choose=int(input("请输入选项："))
      if choose==1:
            function1()
      elif choose==2:
            function2()
      elif choose==3:
            function3()
      elif choose==4:
            function4()
      elif choose==5:
            function5()
      elif choose==6:
            function6()
      elif choose==7:
            function7()
      elif choose==8:
            function8()