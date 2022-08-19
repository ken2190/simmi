from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import ImageModel
from .serializer import ImageSerializer
from rest_framework import viewsets

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    item = ImageModel.objects.all()
    data = {
        'items':item
    }
    return render(request, 'app/home.html', data)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')

    return render(request, 'app/login.html')


def sinup(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('sinup')
            else:
                if  User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists!")
                    return redirect('sinup')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    user.save()
                    messages.success(request, 'You are registered successfully. you are login')
                    return redirect('sinup')
        else:
            messages.error(request, "Password do not match.")
            return redirect('sinup')
    else:
        return render(request, 'app/sinup.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'You are successfully logged out.')
        return redirect('login')
    return redirect('home')


class api(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
