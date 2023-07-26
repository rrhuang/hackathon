# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Transaction

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['face_picture']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['recipient', 'amount']


class VerificationForm(forms.Form):
    face_picture = forms.ImageField()
