from bs4 import BeautifulSoup
import requests
import re
'''
信息的标记：声音，图形，视频，嵌入到文本中
xml：html的通用格式，尖括号标记信息
json：有类型的键值对，支持键值对套用，大括号进行嵌套
ymal：采用键值对，无类型的键值对【缩进代表所属关系】【-号代表并列关系】【|表示整块数据】
'''
def EX_xml():
    '''
        :return:
    '''
    xml_txt='''xml：实例中大部分信息被标签占据
        <person>
            <firstname>Tian</firstname>
            <lastneme>Song</lastneme>
            <address>
                <streeAddr>中关村南大街5号</streeAddr>
                <city>北京</city>
                <zipcode>100081</zipcode>
            </address>
            <prof>Computer System</prof><prof>Security</prof>
        </person>
        '''
    print(xml_txt)
def EX_json():
    '''


    :return:
    '''
    json_txt='''json实例：键值对表示信息，键值对直接需要“”表示类型
    {
    "firstname":"Tian",
    "lastname":"Song",
    "address":{
        "streetAddr":"中关村南大街5号"
        "city":"北京市"
        "zipcode":"100081"
        },
    "prof":["Computer System","Security"]
    }'''
    print(json_txt)
def EX_yaml():
    '''

    :return:
    '''
    yaml_txt='''yaml实例：
    firstname:Tian
    lastname:Song
    address:
        streetAddr:中关村南大街5号
        city:北京市
        zipcode:100081
    prof:
    -Computer System
    -Security
    '''
    print(yaml_txt)
def compare_XJY():
    print('''
        1、XML最早的，扩展好，但标签繁琐
            Internet上信息交互和传递
        2、json：适合js处理，比xml简洁，对值有要求，
            用在程序对接口处理中，但无注释，
        3、yaml：信息无类型，文本保存好，便于阅读
            各类系统配置文件，有注释，易读
        ''')
    print('''
    方法一、完整解析后，获取关键信息，需要标记解析器，
    优点，解析准确
    缺点：繁琐
    
    方法二：直接搜索关键词，无视标记形式
    优点：快
    缺点：不准
    
    结合方式
    ''')
def menu():
    x=(input("请确认是否需要查看信息：（是）"))
    if x=="是":
        EX_xml()
        EX_json()
        EX_yaml()
        compare_XJY()
    else:
        print("end")
def html_findinfo_combine():
    #获取网页信息
    http="http://python123.io/ws/demo.html"
    http2='http://www.baidu.com'
    kv = {'user-agent': 'Mozilla/5.0'}
    r=requests.get(http2,headers=kv)
    #解析
    demo=r.text
    soup=BeautifulSoup(demo,'html.parser')
    # print(soup.text)
    soup.prettify()
    print(soup.find_all(['a','b']))

    for link in soup.find_all('a'):
        print(link.getText('href'))
def html_findinfo_RE():
    '''
    .name
    .atter
    recursive；范围是否是包含所有节点
    :return:
    '''
    http2='http://www.baidu.com'
    kv = {'user-agent': 'Mozilla/5.0'}
    r=requests.get(http2,headers=kv)
    #解析
    demo=r.text
    soup=BeautifulSoup(demo,'html.parser')
    for tag in soup .find_all(re.compile('b')):
        print(tag.name)
if __name__ == '__main__':
    # menu()
    # html_findinfo_combine()
    html_findinfo_RE()