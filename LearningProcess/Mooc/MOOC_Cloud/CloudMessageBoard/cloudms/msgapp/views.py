from datetime import datetime
from django.template import Template,Context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
import os

# Create your views here.
# 用户的请求：提交和获取留言
def homeproc2(request):
    cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response=FileResponse(open(cwd+"/msgapp/templates/111.png",'rb'))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="111.png"'
    '''
    response['Content-Type']='application/octet-stream'
        指定文件类型
    response['Content-Disposition']='attachment;filename="111.png"'
        指定文件名称
        这里是下载的模板
    '''
    return response
def pgproc(request):
    template=Template('<h1>这个程序的名称是{{name}}</h1>')
    context=Context({'name':'实验平台'})
    return  HttpResponse(template.render(context))
def homeproc1(request):
    response=JsonResponse({'key':'value1'})
    return response

def homeproc(request):
    '''
    用来定义根目录的展示内容
    :param request:
    :return:
    '''
    response=HttpResponse()
    response.write("<h1>首页<a href='./msggate'>here</a></h1>")
    return response
    # return HttpResponse("<h1>首页<a href='./msggate'>here</a></h1>")
def msgproc(request):
    datalist = []
    if request.method=='POST':
        userA=request.POST.get('userA',None)
        userB=request.POST.get('userB',None)
        msg=request.POST.get('msg',None)
        time=datetime.now()
        with open('msgapp/templates/msgdata.txt','a+') as f :
            f.write("{}--{}--{}--{}--\n".format(userA,userB,msg,time.strftime("%Y-%m-%d %H:%M:%S")))

    if request.method=='GET':
        d1 = {
            'userA': '胡凯',
            'msg': '测试',
            'time': '2023-06-18 17:54:01'
        }
        # datalist.append(d1)
        userC=request.GET.get('userC',None)
        if userC !=None:
            with open('msgapp/templates/msgdata.txt','r') as f:
                cnt=0
                for line in f:
                    linedata=line.split('--')
                    if linedata[1]==userC or linedata[0]==userC:
                        cnt=cnt+1
                        d={
                            'userA':linedata[0],
                            'msg':linedata[2],
                            'time':linedata[3]
                        }
                        datalist.append(d)
                    if cnt>=10:
                        break
    datalist.reverse()
    return render(request,'MsgSingleWeb.html',{"data":datalist})