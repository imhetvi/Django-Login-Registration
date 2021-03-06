from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.template import Context
# Create your views here.

@login_required
def index(request):
    return render(request, 'userapp/index.html', {'title':'index'})

def register(request):

    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'userapp/register.html', {'form':form, 'title':'register here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            return redirect('index') 
        else: 
            messages.error(request, 'account does not exist, please enter correct username or password') 
    form = AuthenticationForm() 
    return render(request, 'userapp/login.html', {'form':form, 'title':'log in'})

