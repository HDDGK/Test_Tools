import re
def re_info():
    '''
    用来简介表达一组字符串，表示字符串的特征
    .：表示任何单个字符
    []：单个字符的取值范围[abc][a-z][^ab]
    [^]：非
    *：前一个字符0-无限次，abc*=ab,abc,abcc,abccccc...
    +：前一个字符1-无限次,abc+=abc,abcc,abcccc...
    ?：前一个字符0-1次,abc?=ab,abc
    |：左右表达式任意一个 abc|def=abc、def
    {m}：扩展前面字符M次，ab{3}c=abbbc
    {m,n}：扩展前面字符M-n次，ab{1-2}c=abc、abbc
    ^：匹配开头部分，^abc=abc...
    $：匹配结尾部分，$abc=...abc
    ()：分组标记，内部只能使用|，比如(abc)=abc,(abc|def)=abc、def
    \d：数字，等价于[0-9]
    \w：单词字符，等价于[A-Za-Z0-9]
    '''
    print('py开头，不多于10个字符，后续无py:  ', 'PY[^PY]{0,10}')
    print('26个字母组成的字符串，可以这样表示', '^[A-Za-z]+$')
    print('26个字母+数字组成的字符串，可以这样表示', '^[A-Za-z0-9]+$')
    print('整数形式的字符串', '^-?\d+$')
    print('正整数形式的字符串', '^[0-9]*[1-9][0-9]*$')
    print('是否中文', '\\u4e00-\\u9fa5')
    print("国内电话号码", "\d{3}-\d{8}|\d{4}-\d{7}")
    print('IP 地址', "")


def main():
    '''
    re.serch：字符串中搜索符合正则表达式的第一个位置，返回match
    pattern:正则表达式
    string：匹配字符串
    flags：控制标记
        re.I 忽略大小写
        re.M:正则表达式的^操作符能够将给定字符串的每行当做匹配开始
        re.S:正则表达式中的.操作符能够匹配所有字符，【默认匹配除换行外所有字符】
    '''
    match=re.search(r'[1-9]\d{5}','BIT 100081')
    if match:
        print(match.group(0))

    '''
    re.match：字符串第一个位置匹配正则表达式，返回match
    '''
    match2=re.match(r'[1-9]\d{5}','100081 BIT 100081')
    if match2:
        print(match2.group(0))
        print("a")
    print(type(match2),match2.string,match2.re,match2.pos,match2.endpos)
    print(match2.group(0),match2.start(),match2.end(),match2.span())


    '''
    re.findall：搜索字符串，返回列表类型
    '''
    match3=re.findall(r'[1-9]\d{5}','100081 BIT 100081')
    print(match3)

    '''
    re.split：按正则表达式分割字符，返回，列表
    '''
    match4=re.split(r'[1-9]\d{5}','100081 BIT 100081',maxsplit=1)
    print(match4)

    '''
    re.finditer：搜索字符串，返回匹配结果的迭代类型，每个迭代元素是match
    '''
    for m in re.finditer(r'[1-9]\d{5}','100081 BIT 100081'):
        if m:
            print(m.group(0))

    '''
    re.sub：在一个字符串中替换所以匹配的正则表达式的子串，返回替换后的字符串
    :return:
    '''
    match5=re.sub(r'[1-9]\d{5}',":zip",'100081 BIT 100081')
    print(match5)


def runonce():
    rst=re.search(r'[1-9]\d{5}','100081 BIT 100081')


def runrun():
    '''
    面向对象，一次编译成对象，多次调用
    pat=re.compile(r'[1-9]\d{5}')
    对象有对应的操作方法
    :return:
    '''
    pat=re.compile(r'[1-9]\d{5}')
    rst=pat.search('100081 BIT 100081')


def maxRE():
    match=re.search(r'PY.*N','PYANBNCNDN')
    print(match.group(0))


def minRE():
    match = re.search(r'PY.*?N', 'PYANBNCNDN')
    match = re.search(r'PY.+?N', 'PYANBNCNDN')
    match = re.search(r'PY.??N', 'PYANBNCNDN')
    match = re.search(r'PY.[0-1]?N', 'PYANBNCNDN')
    print(match.group(0))


if __name__ == '__main__':
    main()
    runonce()
    runrun()
    maxRE()
    minRE()
    '''
    两种对应的使用方式
    最大匹配和最小匹配
    几种方法之间的区别
    '''