import re
#----------正则表达式RE------------

#----------------元字符----------------
#^表示查行的开始，$表示查行的结尾，如果没有说明则查任意部分
#\b 插入匹配点，开始或者结束
#\w 匹配任意字母和字符等，加*代表任意个
#\s 匹配任意空白
#\d 匹配任意数字

#----------------限定符----------------
#匹配之前的字符
# ? 【0-1】次
# + 【1-∞】次
# * 【0-∞】次
# {n} 【n】次
# {n,} 至少【n】次
# {n,m} 至少【n】次，至多【m】次

#字符类
#【aeiou】匹配其中字母
#【.？!】匹配其中符号
#【a-z0-9A-Z】匹配其中字母
#【^a-z0-9A-Z】不匹配其中字母
# | 选择字符，同时选择多个条件
# \ 转义字符，\.转义符号
#(thir|four)th ()起到限定范围
# r'.....' r为原生字符，避免转义斜杠过多

#RE模块
pattern=r'mr_\w*'
String1=r'MR_Chicken mr_chicken'
String2=r'MR_Chickenmr_chicken&mr_chicken'
String3=r'MR_Chicken?mr_chicken!mr_chicken'
mathc=re.match(pattern,String1,re.I)
print(mathc.group())
mathc2=re.match(pattern,String2,re.I)
print(mathc2.group())

#match和serch的区别，前者查是否以什么开头，serch则是查询第一次出现，并返回
math3=re.search(pattern,String1,re.I)
print(math3.group())
math4=re.search(pattern,String2,re.I)
print(math4.group())

math5=re.findall(pattern,String1)
print(math5)
math6=re.findall(pattern,String2)
print(math6)

#替换字符
result=re.sub(pattern,"BAC",String3)
print(result)

#分割字符
pattern2=r'[?|!]'#这里没有【】限制范围的话会报错
math7=re.split(pattern2,String3,3)
print(math7)

