from django.urls import path
from . import views
'''
路由机制
URL-[定义、转换、传参、命名等]-views
路由是：关联URL，及其处理函数的过程
    工程的settings.py中的ROOT_URLCONF变量指定全局路由文件，知道工程的第一个入口路由文件在哪里
    urlpatterns表示路由定义关系
        path(route,views)：字符串类型的路由
        re_path(route,views)：RE正则表达式的路由
        在全局路由中逐个排查
        Django只关心URL
        
        route的三种格式
            精确字符串：articles/2003/
                静态URL响应：一个URL对应一个操作函数
                
            Django的转换格式：<类型:变量>   articles/<int:year>/
                URL部分信息为参数：通过URL进行参数传递【articles/2003/————articles/<int:year>/】其中year：2003
                    str、int、slug、uuid、path
                
            正则表达式：articles/(?P<year>[0-9]{4})/
                选择符合标准的字符串
                
        view 处理函数和include()
            include
                附加本地路由
                可以进行路径去重，路径前缀去重，提前相同前缀，
        URL的根目录处理
            ''、'^$',都可以代表空目录。
'''