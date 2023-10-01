"""
URL configuration for cloudms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from msgapp import views as msgviews

urlpatterns = [
    path('msggate/',include('msgapp.urls')),
    # 全局路由增加对本地路由对接

    path('admin/', admin.site.urls),
    path('',msgviews.homeproc),
    path('playground',msgviews.pgproc),
    # path('',msgviews.homeproc1),
    #homeproc1是返回了键值对
    # path('',msgviews.homeproc2),
    #homeproc2是返回file下载
]
