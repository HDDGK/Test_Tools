import os.path

filename = "student.txt"


def insert():
    student_list = []
    while True:
        id = input("请输入ID（例如：1001）：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            English = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            java = int(input("请输入Java成绩："))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue
        student = {'ID': id,
                   'NAME': name,
                   'ENGLISH': English,
                   'PYTHON': python,
                   'JAVA': java}
        student_list.append(student)
        answer = input('您确定是要继续吗？【Y/y】')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)


def save(list):
    try:
        stu_txt = open(filename, "a", encoding='utf-8')
    except:
        stu_txt = open(filename, "w", encoding='utf-8')
    for item in list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()
    print("学生信息录入完毕")


def show_student(list):
    if len(list)==0:
        print("没有查到信息")
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语','Python','Java','总成绩'))
    for item in list:
        print(format_title.format(item.get('ID'),
                                  item.get('NAME'),
                                  item.get('ENGLISH'),
                                  item.get('PYTHON'),
                                  item.get('JAVA'),
                                  int(item.get('ENGLISH')+item.get('PYTHON')+item.get('JAVA'))
                                  ))


def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=eval(input('按ID查找请输入1，按姓名查找请输入2：'))
            if mode==1:
                id = input("请输入学生ID")
            elif mode==2:
                name = input("请输入学生姓名")
            else:
                print('你输入的有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!="":
                        if d['ID']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['NAME']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('您确定是要继续吗？【Y/y】')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break



def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入需要修改的ID（例如：1001）：")
    print(student_id)
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            print(d)
            print(d['ID'])
            if d['ID'] == student_id:
                print("找到学生")
                while True:
                    try:
                        d["NAME"] = input("请输入姓名：")
                        d['ENGLISH'] = int(input("请输入英语成绩："))
                        d['PYTHON'] = int(input("请输入Python成绩："))
                        d['JAVA'] = int(input("请输入Java成绩："))
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                wfile.write(str(d) + '\n')
                print("修改成功")
            else:
                wfile.write(str(d) + '\n')
        answer = input('您确定是要继续吗？【Y/y】')
        if answer == 'y' or answer == 'Y':
            modify()
def delete():
    while True:
        student_id = input("请输入需要删除的ID（例如：1001）：")
        if student_id != "":
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readline()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['ID'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f"ID为{student_id}的学生已经删除。")
                    else:
                        print(f"ID为{student_id}的学生没有找到。")
            else:
                print("目前无学生信息了")
                break
            show()
            answer = input('您确定是要继续吗？【Y/y】')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def sort():
    global asc_or_desc_bool
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students_list = rfile.readlines()
        students_new=[]
        for item in students_list:
            d=dict(eval(item))
            students_new.append(d)
    else:
        return
    asc_or_desc=input("请选择（0升、1降）：")
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print("您输入模式有误，请重新输入")
        sort()
    mode=eval(input("请选择（1英语、2Python、3Java、4总）："))
    if mode ==1:
        print(1)
        students_new.sort(key=lambda x:int(x['ENGLISH']),reverse=asc_or_desc_bool)
    elif mode==2:
        students_new.sort(key=lambda x:int(x['PYTHON']),reverse=asc_or_desc_bool)
    elif mode==3:
        students_new.sort(key=lambda x:int(x['JAVA']),reverse=asc_or_desc_bool)
    elif mode==4:
        students_new.sort(key=lambda x:int(x['ENGLISH']+x['PYTHON']+x['JAVA']),reverse=asc_or_desc_bool)
    elif mode==0:
        pass
    else:
        print("您输入的模式有误，请重新输入")
        sort()
    show_student(students_new)

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print("还没有录入学生信息")
    else:
        print("暂未保存数据信息")


def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)

    else:
        print("暂未保存数据信息")

def menu():
    tab = '\t' *3
    menuList = ["1、录入学生信息",
                "2、查找学生信息",
                "3、删除学生信息",
                "4、修改学生信息",
                "5、排序学生信息",
                "6、统计学生总数",
                "7、显示学生信息",
                "0、退出"
                ]
    print("=" * 22 + "学生信息管理系统" + "=" * 22)
    print("-" * 25 + "功能菜单" + "-" * 25)
    for i in menuList:
        print(tab + i)
    print("-" * 58)
    # print(tab,'1、录入学生信息')


'''
    print(tab,'2、查找学生信息')
    print(tab,'3、删除学生信息')
    print(tab,'4、修改学生信息')
    print(tab,'5、排序学生信息')
    print(tab,'6、统计学生总数')
    print(tab,'7、显示学生信息')
    print(tab,'0、退出')
'''


def main():
    while True:
        menu()
        choice = int(input("请选择："))
        # if choice in [0,1,2,3,4,5,6,7]:
        if choice in range(0, 8):
            if choice == 0:
                answer = input('您确定是要退出系统吗？【Y/y】')
                if answer == 'y' or answer == 'Y':
                    print("感谢使用！！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


main()
