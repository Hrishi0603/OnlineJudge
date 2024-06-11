from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def register_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists(): 
            messages.info(request, 'Username taken')
            return redirect("/auth/register/")
        
        user = User.objects.create_user(username = username)

        user.set_password(password)
        user.save()
        messages.info(request,'User created successfully!')
        return redirect('/auth/register/')
    
    context = {}
    return render(request, "register.html", context)

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login/')
        

        login(request,user)
        messages.info(request,'login successful')

        return redirect('/home/topics/')
    
    context ={}
    return render(request, "login.html", context)   #Why is this at the end?

def logout_user(request):
    logout(request)   #What does this do?
    messages.info(request,'logout successful')
    return redirect('/auth/login/')

