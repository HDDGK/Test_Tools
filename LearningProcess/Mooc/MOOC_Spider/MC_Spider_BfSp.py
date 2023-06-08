import requests
from bs4 import BeautifulSoup
def tryBeautifulSoup():
    #获取网页信息
    http="http://python123.io/ws/demo.html"
    r=requests.get(http)
    #解析
    demo=r.text
    soup=BeautifulSoup(demo,'html.parser')
    soup2=BeautifulSoup(demo,'xml')
    soup3=BeautifulSoup(demo,'lxml')
    soup4=BeautifulSoup(demo,'html5lib')
    print(soup.prettify())
    print(soup.title)
    print(soup.a)
    tag=soup.a
    print(tag.attrs)
    print("--------------------")
    print(tag.attrs['class'])
    print(tag.attrs['href'])
    print("--------------------")
    print(type(tag.attrs))
    print(type(tag))
    print(soup.a.name)
    print(soup.a.parent.name)
    print(soup.a.parent.parent.name)
    print(soup.a.name)
    print(soup.p)
    print(soup.p.string)
    #跨了多个标签
    print(type(soup.p.string))
    '''
    bs4.html解析器html.parser：
    lxml的解析器lxml和xml：pip install lxml
    html5lib的解析器html5lib：pip install html5lib
    '''


def tryBeautifulSoup_comment():
    newsoup=BeautifulSoup("<b><!--你好--></b><p>我不是标签</p>",'html.parser')
    print(newsoup.string)
    print(newsoup.b.string)
    #注释为标明，需要按标签判断
    print(type(newsoup.b.string))
    print(newsoup.p.string)
    print(type(newsoup.p.string))
    '''
    Tag：标签
    Name：标签名字xx.name
    Attributes：标签属性，字典 XX.attrs
    NavigableString：标签非属性字符串
    Comment：标签内注释
    '''


def show_BeautifulSoup():
    http = "http://python123.io/ws/demo.html"
    r = requests.get(http)
    # 解析
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    #3种遍历
    print("下行遍历--------------开始")
    #下行遍历
    '''
    .contents：子节点的列表
    .children：子节点的迭代类型，与contents类似，，包含子节点，用于遍历
    .descendants：子孙节点，包含所有子孙节点，用于遍历
    '''

    print(soup.head)
    print(soup.head.contents)
    print(soup.body.contents)
    print(len(soup.body.contents))

    for i in range(len(soup.body.contents)) :
        if soup.body.contents[i]=="\n":
            print("",end="")
        else:
            print(soup.body.contents[i])

    print("下行遍历--------------结束")
    print("上行遍历--------------开始")
    #上行遍历
    '''
    .parent：
    .parents：
    '''
    print(soup.title.parent)
    print()
    print(soup.html.parent)
    print()
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
    print("上行遍历--------------结束")
    print("平行遍历--------------开始")
    '''
    前提是在同一父结点下
    .next_sibling：返回下一个平行节点的标签
    .previous_sibling：返回上一个平行节点的标签
    .next_siblings：返回后续所有平行节点的标签
    .previous_siblings：返回之前所有平行节点的标签
    '''
    print(soup.a.next_sibling)
    print(soup.a.next_sibling.next_sibling)
    print(soup.a.previous_sibling)
    print(soup.a.previous_sibling.previous_sibling)

    for i in soup.a.next_siblings:
        print(i)
    print("平行遍历--------------结束")


def show_HTML():
    '''
    友好展示

    :return:
    '''
    http = "http://python123.io/ws/demo.html"
    r = requests.get(http)
    # 解析
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    soup.prettify()#标签后\n，优化展示
    print(soup.prettify())

if __name__ == '__main__':
    tryBeautifulSoup()
    tryBeautifulSoup_comment()
    show_BeautifulSoup()
    show_HTML()