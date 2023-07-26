# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm
from .forms import TransactionForm
from .models import Transaction
from .forms import VerificationForm
from .models import Transaction
import face_recognition

def index(request):
    return render(request, 'app/index.html')

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})


def home(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.sender = request.user
            transaction.save()
            return redirect('verify', transaction_id=transaction.id)
    else:
        form = TransactionForm()
    return render(request, 'home.html', {'form': form})


