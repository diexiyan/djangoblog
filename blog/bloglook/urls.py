from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from . import models

app_name = 'bloglook'

urlpatterns = [
    url(r'^(\d*)/*(\d*)$', views.index, name='index'),
    # url(r'^$', views.index, name='index'),
    url(r'^show/(\d+)/$', views.show, name='show'),
    url(r'^type/(\d+)/', views.type, name='type'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'pubcom/(\d+)/$', views.pubcom, name='pubcom'),
    url(r'^time/(\d+)/$', views.time, name='time'),
]
