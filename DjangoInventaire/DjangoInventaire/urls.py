"""DjangoInventaire URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from inv.views import ItemListView, ItemCreateView, ItemRetrieveView,ItemUpdateView, ItemDeleteView , ItemLoginView, ItemLogoutView
from django.conf.urls import patterns, include, url

from django.contrib.auth.decorators import login_required

items_urls = [
    url(r'create/', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ItemRetrieveView.as_view(), name='retrieve'),
    url(r'^(?P<pk>\d+)/update/', ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/', ItemDeleteView.as_view(), name='delete'),
   
] 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ItemListView.as_view(), name='items-list'),
    url(r'^items/', include(items_urls, namespace='items')),
    url(r'^login/', ItemLoginView.as_view(), name='login'),
    url(r'^logout/$', ItemLogoutView.as_view(), name='logout'),
   
]

