"""djangoProject117 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myInfo import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('info', views.info,  name ='info'),
        path('', views.home,  name='home'),
        path('profile', views.profile,  name='profile'),
        path('Interest', views.Interest,  name='Interest'),
        path('Educational', views.Educational, name='Educational'),
        path('Career', views.Career,  name='Career'),
        path('RoleModel', views.RoleModel, name='RoleModel'),
        path('Article', views.Article, name='Article'),
        path('showA1', views.showA1, name='A1'),
        path('showA2', views.showA2, name='A2'),
        path('showA3', views.showA3, name='A3'),
        path('showA4', views.showA4, name='A4'),
        path('showA5', views.showA5, name='A5'),
        path('showA6', views.showA6, name='A6'),
        path('showA7', views.showA7, name='A7'),
        path('showA8', views.showA8, name='A8'),
        path('etc', views.etc, name='etc'),
        path('resume', views.resume, name='resume'),
        path('showMyData', views.showMyData, name='myLab10'),
        path('showDataCamera', views.showDataCamera, name='myLab11'),
        path('test', views.test, name='test'),
        path('goods', views.showGoods, name='goods'),
        path('<gid>/showOneGoods', views.showOneGoods, name='showOneGoods'),
        path('newGoods', views.newGoods, name='newGoods'),
        path('<gid>/updateGoods', views.updateGoods, name='updateGoods'),
        path('<gid>/deleteGoods', views.deleteGoods, name='deleteGoods'),
        path('Customer', views.showCustomer, name='Customer'),
        path('<cid>/showOneCustomer', views.showOneCustomer, name='showOneCustomer'),
        path('newCustomer', views.newCustomer, name='newCustomer'),
        path('<cid>/updateCustomer', views.updateCustomer, name='updateCustomer'),
        path('<cid>/deleteCustomer', views.deleteCustomer, name='deleteCustomer'),



]

