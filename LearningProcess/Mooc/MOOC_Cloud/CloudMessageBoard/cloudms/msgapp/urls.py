from django.urls import path
from . import views
urlpatterns=[
    path('',views.msgproc),
]#增加对本地路由的支持，