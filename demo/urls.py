"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from demo1 import views
from django.http import request
from django.contrib import admin

user_partterns = [
    url(r'^login', views.login),
]

two_patterns = [
    url(r'^user/',include(user_partterns)),
]
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', include(two_patterns)),
    url(r'^web/', views.myWebInternet),
]


