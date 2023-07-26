# views.py
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
import face_recognition

def index(request):
    return render(request, 'app/index.html')
def signup(request, error_msg=''):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            face_picture = form.cleaned_data.get('face_picture')

            user = authenticate(username=username, password=raw_password)

            try:
                addUser(first_name, last_name, email, face_picture)
            except Exception as e:
                return signup(request, error_msg="Error: There is a database error in adding this user: " + str(e))
            
            
            #login(request, user)
            return redirect('index')
                        
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


from django.contrib.auth.forms import AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('success')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def success(request):
    if request.user.is_authenticated:
        return render(request, 'success.html')
    else:
        return redirect('accounts/login')
    
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def main_page(request):
    return render(request, 'main_page.html')


@login_required(login_url='/accounts/login/')
def send_money(request):
    if request.method == 'POST':
        form = SendMoneyForm(request.POST)
        if form.is_valid():
            return redirect('authauth')
    else:
        form = SendMoneyForm()
    return render(request, 'send_money.html', {'form': form})    

@login_required(login_url='/accounts/login/')
def authauth(request):
    return render(request, 'authauth.html')

def successful(request):
    return render(request, 'successful.html')





