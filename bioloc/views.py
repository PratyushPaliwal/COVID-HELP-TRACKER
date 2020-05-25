from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def bioloc(request):
    return render(request, 'entry.html')

def mapit(request):
    a = request.user
    if request.method == 'POST':
        
        #b = User.objects.get(first_name = 'a')
        a.profile.bio = request.POST['bio']
        a.profile.lattitude = request.POST['latitude']
        a.profile.longitude = request.POST['longitude']
        print('going ro mapit')
        
        a.save()
        users = User.objects.all()
        return render(request, 'index.html',{'users': users})
    else:
        users = User.objects.all()
        return render(request, 'index.html',{'users': users})
       
def logout(request):
    auth.logout(request)
    return redirect('/')

def testing(request):
    a = request.user
    if request.method == 'POST' :
        print('going in testing')
        lat = request.POST['json.latitude']
        lon = request.POST['json.longitude']
        a.profile.longitude = lon
        a.profile.latitude = lat 
        a.save()
       
  