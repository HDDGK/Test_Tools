import urllib3
import json

String_Chooice = ['Ullib3：',
                  '[1]GET请求',
                  '[2]POST请求',
                  '[3]获取响应头',
                  '[4]JSON',
                  '[5]二进制图片',
                  '[6]复杂请求',
                  '[7]代理IP',
                  '[8]上传文件',
                  ]
url_Get= 'https://www.httpbin.org/get'
url_Post='https://www.httpbin.org/post'
url_Python= 'https://www.Python.org/'
url_baidu= 'https://www.baidu.com/'
url_PNG='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
url_Proxy='http://httpbin.org/ip'
url_PutFile='http://httpbin.org/post'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def ullib3_GET():
    #创建连接池，管理对象
    http = urllib3.PoolManager()

    #发送Get请求，针对不同的网页请求
    r = http.request('GET', url_Get)
    r_Python = http.request('GET', url_Python)
    r_baidu = http.request('GET', url_baidu)

    #打印发送请求的结果
    print(r.status)
    print(r_Python.status)
    print(r_baidu.status)


def ullib3_POST():
    urllib3.disable_warnings()#关闭SSL告警
    params={'name':'jack','country':'中国','age':'30'}#定义字典型请求参数，【还有列表和其他类型# 】
    http=urllib3.PoolManager()#创建连接池，管理对象，这里要理解一下P开头大小和小写，我觉得这里是参数和方法的区别
    r=http.request('POST',url_Post,fields=params)#发送POST请求
    print('返回结果:',r.data.decode('unicode_escape'))
    #这里decode('unicode_escape')和'utf-8'区别是，上传的表单的内容展现的方式


def ullib3_GetHeader():
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    # 发送Get请求，针对不同的网页请求
    r = http.request('GET', url_Get)
    reponse_header=r.info()
    for key in reponse_header.keys():
        print(key,':',reponse_header.get(key))


def ullib3_JSON():
    urllib3.disable_warnings()  # 关闭SSL告警
    params = {'name': 'jack', 'country': '中国', 'age': '30'}  # 定义字典型请求参数，【还有列表和其他类型# 】
    http = urllib3.PoolManager()  # 创建连接池，管理对象，这里要理解一下P开头大小和小写，我觉得这里是参数和方法的区别
    r = http.request('POST', url_Post, fields=params)  # 发送POST请求,方法+地址+参数
    j=json.loads(r.data.decode('Unicode_escape'))
    print("数据类型：",type(j))
    print("获取的form对应的数据：",j.get('form'))
    #注意form和from
    print("获取的country对应的数据：",j.get('form').get('country'))

    # 这里decode('unicode_escape')和'utf-8'区别是，上传的表单的内容展现的方式


def ullib3_2JingZhi():
    urllib3.disable_warnings()  # 关闭SSL告警
    http = urllib3.PoolManager()  # 创建连接池，管理对象，这里要理解一下P开头大小和小写，我觉得这里是参数和方法的区别
    r = http.request('GET', url_PNG)  # 发送POST请求,方法+地址+参数
    print(r.data)
    f=open('Python.png','wb+')
    f.write(r.data)
    f.close()


def ullib3_GET2():
    urllib3.disable_warnings()  # 关闭SSL告警
    http=urllib3.PoolManager()
    r=http.request('GEt', url_Get, headers=headers, timeout=urllib3.Timeout(connect=1, read=0.5))
    print(r.data.decode('utf-8'))


def ullib3_SetProxy():
    proxy=urllib3.ProxyManager('https://120.27.110.144:80',headers=headers)
    r=proxy.request('get',url_Proxy,timeout=6)
    print(r.data.decode())


def ullib3_PutFile():
    with open('text.txt')as file_Txt:
        file_Data=file_Txt.read()
    http=urllib3.PoolManager()
    r=http.request('Post',url=url_PutFile,fields={'filefield':('example.txt',file_Data),})
    files=json.loads(r.data.decode('utf-8'))['files']
    print(files)

    with open('Python.png','rb')as file_Png:
        file_Data2=file_Png.read()
    http=urllib3.PoolManager()
    r=http.request('Post',url=url_PutFile,body=file_Data2,headers={'Content-Type':'image/jpeg'})
    print(r.data.decode())



if __name__=='__main__':
      for i in String_Chooice:
            print(i)
      choose=int(input("请输入选项："))
      if choose==1:
            ullib3_GET()
      elif choose==2:
            ullib3_POST()
      elif choose==3:
            ullib3_GetHeader()
      elif choose==4:
            ullib3_JSON()
      elif choose==5:
            ullib3_2JingZhi()
      elif choose==6:
            ullib3_GET2()
      elif choose==7:
            ullib3_SetProxy()
      elif choose==8:
            ullib3_PutFile()

