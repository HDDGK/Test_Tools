def str_format():
    # 字符串的格式化
    name = input("请输入你的名字:")
    address = input("请输入你的地址:")
    age = int(input("请输入你的年龄:"))
    hobby = input("请输入你的爱好:")
    # %s 占位字符串
    # %d 占位整数
    # %f 占位小数
    s = "我叫%s，我住在%s，我今年%d岁，我喜欢%s" % (name, address, age, hobby)
    s0 = "我叫%s" % name
    s1 = "\n我叫{}，我住在{}，我今年{}岁，我喜欢{}".format(name, address, age, hobby)
    s2 = f"\n我叫{name}，我住在{address}，我今年{age}岁，我喜欢{hobby}"
    print(s,s0, s1, s2)

def str_cut():
    # 索引和切片
    s = "我叫周杰伦，你呢，你叫周润发？"
    print(s[-1])
    print(s[0:5])#后面娶不到
    print(s[:5])
    print(s[6:])
    print(s[:])
    print(s[-3:-1])
    print(s[-1:-3])#无结果，-1往右切不到-3
    print(s[::-1])#步长=-1，从右往左切
def str_change():
    s='\npython have a dream'
    print(s.capitalize(),s.title(),s)
    s1='\nPYTHON HAVE A DREAM'
    print(s.lower())
    print((s.lower()).upper() )

def str_strip():
    s="    你好，   我叫  周杰伦  "
    s1=s.strip()
    print(s1)

def str_findstr():
    s="你好呀，我叫周杰伦"
    ret=s.find("周润发")
    ret2=s.index("周杰伦")
    print(ret,ret2)
    print("周杰伦" in s)
    if s.startswith("你"):
        if s.endswith("伦"):
            print("你伦")
    inp=input("")
    if inp.isdigit():
        print("整数",inp)
    elif inp.isdecimal():
        print("小数",inp) 
def ex_compare():
    verify_code='aSdc'
    user_input=input(f'请输入验证码（{verify_code}）:')
    user_input=user_input.strip()
    if verify_code.upper()==user_input.upper():
        print("pass")
    else:
        print('fail')

if __name__ == '__main__':
    # str_format()
    # str_cut()
    # str_change()
    # ex_compare()
    str_findstr()