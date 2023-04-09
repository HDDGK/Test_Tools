
def division():
    '''分苹果'''
    apple=int(input("输入苹果数量"))
    childen=int(input("输入小孩子的个数"))
    result_division=int (apple/childen)
    # if apple<childen:
    #     #下面raise是在方法中就提前限制，而不是在使用中才单个使用单个限制
    #     raise ValueError("苹果应该比人多")

    #相较于print来打印异常步骤，在方法中，易出问题点，查一个判断，触发时弹出对应报错
    #且相较于上面的提前报错，assert更精准，且可以自定义对应的报错信息
    assert apple > childen,"苹果不够分，这里使用assert的话更精准，且可以自定义对应的报错信息"

    next_apple=apple-childen*result_division
    if  next_apple>0:
        print(str(apple)+"个苹果分给"+str(childen)+"个小朋友，每个人可以拿到"+str(result_division)+"个苹果，最后剩下"+str(next_apple)+"个")
    else:
        print(str(apple) + "个苹果分给" + str(childen) + "个小朋友，每个人可以拿到" + str(result_division) + "个苹果")

if __name__=='__main__':
    try:
        division()


    except AssertionError as e:
        print("输入有误：",e)
        #这里不能用+连接，会报错，TypeError: can only concatenate str (not "AssertionError") to str
    except ZeroDivisionError:
        print("这里小朋友为0还分个锤子")
        print("这里要小心除0错误：ZeroDivisionError: division by zero")
    # except ValueError:
    #     print("需要注意这里输入的苹果和人的数量都需要为整数，且苹果数量要比人多才行")
    else:
        print("分苹果大业顺利完成，只有没有报错才能到我这里")
    finally:
        print("这里进行了分苹果操作，无论成败我都会出现")
