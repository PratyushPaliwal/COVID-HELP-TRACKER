from django.urls import path
from . import views

urlpatterns = [
    path('',views.bioloc, name= 'bioloc'),
    path('mapit', views.mapit, name='mapit'),
    path('test', views.testing, name = 'test'),
    path('logout', views.logout, name = 'logout')
]
  