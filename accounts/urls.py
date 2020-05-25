from django.urls import path
from . import views

urlpatterns = [
    path('', views.authen, name='authen')
   
]
