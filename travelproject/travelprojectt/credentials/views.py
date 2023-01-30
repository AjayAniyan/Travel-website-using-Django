from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password1']
        if password == confirmpassword:
            if User.objects.filter(username =username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "email already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
