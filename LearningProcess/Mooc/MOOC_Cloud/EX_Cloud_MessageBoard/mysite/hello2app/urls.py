from django.urls import path
from . import views
urlpatterns=[
    path('', views.hello)
    #本地路由
]