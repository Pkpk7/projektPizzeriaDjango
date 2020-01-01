from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax', views.ajax, name='ajax'),
    path('zaloguj', views.zaloguj, name='zaloguj'),
    path('index2', views.index2, name='index2'),
    path('admin', views.admin, name='admin')
]