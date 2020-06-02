"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.login, name='login'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('home/', views.home, name='home'),

    path('user/', views.user, name='user'),

    # 添加带有字符类型/整型和slug的url
    # path('<year>/<int:month>/<slug:day>',views.mydate)
    # 正则表达式规范格式

    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate, name='mydate'),

    re_path('dict/(?P<year>[0-9]{4}).html', views.myyear_dict, {'month': '07'}, name='myyear_dict'),

    path('download.html', views.download),
]
