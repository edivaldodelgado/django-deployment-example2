from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from basicApp import views

# TEMPLATE TAGGING
app_name = 'basicApp'

urlpatterns = [
    url(r'^relative/$',views.relative, name='relative'),
    url(r'^other/$',views.other, name='other'),
]
