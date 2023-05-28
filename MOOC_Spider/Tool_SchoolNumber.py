import time

import bs4.element
import requests
import bs4
from bs4 import BeautifulSoup
import os
'''
实例：获取网页大学排名信息
对应网站的时间2023.5.28
'''


def getHtmlText(url):
    try:
        kv={'user-agent': 'Mozilla/5.0'}
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        # print(r.text)
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    # print("？")
    # print(soup)
    # soup.prettify()
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            # print("有了")
            tds=tr('td')
            '''
            #验证是否可以正常加载信息
            print("排名",tds[0].text.strip())
            print("学校",tr.find_all('a')[0].text.strip())
            print("名称",tr.find_all('a')[1].text.strip())
            print("省市",tds[2].text.strip())
            print("类型",tds[3].text.strip())
            print("总分",tds[4].text.strip())
            print("层次",tds[5].text.strip())
            print(type(str(tds[0].text.strip())))
            print(type(tds[5].text.strip()))
            '''
            links=tds[1].findNext("img")
            link=links.get('src')
            print(link)
            school_DownloadPicture(link,tr.find_all('a')[0].text.strip())
            ulist.append([tds[0].text.strip(),tr.find_all('a')[0].text.strip(),tr.find_all('a')[1].text.strip(),tds[2].text.strip(),tds[3].text.strip(),tds[4].text.strip(),tds[5].text.strip()])

    print("OK")
def school_DownloadPicture(url,name):
    kv2 = {'user-agent': 'Mozilla/5.0'}
    root=r"C:\Users\HK145-TP\Desktop\新建文件夹\学校图标\\"
    autoPath=root+name+"."+(url.split("/")[-1]).split(".")[-1]
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


def printUnivList(ulist,num):
    # print("{:^4}\t{:^10}\t{:^4}\t{:^4}\t{:^10}\t{:^5}\t{:^10}".format("排名","学校名称", "省市","类型","总分","办学层次","英文名称"))
    print("{0:^4}\t{1:^10}\t{2:^4}\t{3:^4}\t{4:^10}\t{5:^5}\t{6:^10}".format("排名","学校名称", "省市","类型","总分","办学层次","英文名称",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print("{:^4}\t{:^10}\t{:^4}\t{:^4}\t{:^10}\t{:^5}\t{:^10}".format(u[0], u[1], u[3], u[4], u[5], u[6], u[2]))
    print('suc'+str(num))
def main(url_list):
    for url in url_list:
        uinfo = []
        Html_txt = getHtmlText(url)
        fillUnivList(uinfo, Html_txt)
        printUnivList(uinfo, 30)

def formatString():
    # print("{:^4}\t{:^10}\t{:^4}\t{:^4}\t{:^10}\t{:^5}\t{:^10}".format("排名", "学校名称", "省市", "类型", "总分", "办学层次", "英文名称"))s
    print("{0:^4}\t{1:{2}^10}".format("排名", "学校名称",chr(12288)))


if __name__ == '__main__':
    url_list = ['https://www.shanghairanking.cn/rankings/bcur/2023',]
    try:
        main(url_list)
    except:
        x=input("是否重新链接：（Y/N）")
        if x=="Y" or 'y':
            main(url_list)
        else:
            print("再检查一下")
    # formatString()#测试一下打印，没有使用

