from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from calendarapp.forms import SignupForm


def signup(request):
    forms = SignupForm()
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            # messages.info(request,'ไม่พบข้อมูล')
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('calendarapp:calendar')
    context = {'form': forms}
    
    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return redirect('signup')


def calendar (request):
    return render (request, 'calendar.html')


def todolist (request):
    return render (request, 'todolist.html')


def createForm (request):
    return render (request, 'register.html')


def loginForm (request):
    return render (request, 'signup.html')


def register (request):
    return render (request, 'register.html')


def addUser (request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password ==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request, 'UserName นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
            )
            user.save()
            return redirect('/')
    else :
        messages.info(request, 'รหัสผ่านไม่ตรงกัน')
        return redirect('/createForm')
