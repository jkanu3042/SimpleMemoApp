"""SimplePhotoMemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.memo_list , name='memo_list'),
    url(r'^memo/create/$', views.memo_create, name='memo_create'),
    url(r'^memo/(?P<pk>\d+)/$', views.memo_detail, name='memo_detail'),
    url(r'^memo/(?P<pk>\d+)/edit/$', views.memo_edit, name='memo_edit'),
    url(r'^memo/(?P<pk>\d+)/delete/$', views.memo_delete, name='memo_delete'),

]
