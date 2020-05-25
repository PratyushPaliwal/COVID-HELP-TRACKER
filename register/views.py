
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone= request.POST['phone']
        is_helper = request.POST['is_helper']
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        #email= request.POST['email']

     
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            #elif User.profile.objects.
             #   messages.info(request, 'phone taken')
              #  return redirect('register')
            #elif User.objects.filter(phone=phone).exists():
             #   messages.info(request, 'phone taken')
              #  return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password1,first_name=first_name, last_name= last_name)
               # profile = request.user.get_profile()
                user.profile.phone = phone
                user.profile.is_helper = is_helper
                user.save()
               
                messages.info(request,'user created')
                return redirect('login')
               
        else:
            messages.info(request,'password not matching')
            return redirect('register')

    else:
        return render(request, 'login.html')

