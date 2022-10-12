# from crypt import methods
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,'testapp/index.html')
def singup(request):
    if request.method =='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['Pass1']
        pass2=request.POST['Pass2']
        # print(username.data())
        # user=username,fname,lname,email,pass1,pass2
        myuser=User.objects.create_user(username,email,pass1)
        # print(myuser)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'your account has been create')
        return redirect(singin)
    else:
        return render(request,'testapp/singup.html')
def singin(request):
    if request.method =='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'testapp/index.html',{'fname':fname})
        else:
            messages.error(request,'bad credential')

            return redirect('home')
    return render(request,'testapp/singin.html')
def singout(request):
    logout(request)
    messages.success(request,'suceesfully logout')
    return redirect('home')

