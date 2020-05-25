
from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from django.contrib.auth.models import User,auth
#from django.contrib import messages
# Create your views here.
def authen(request):
    return render(request, 'login.html')

# Create your views here.
