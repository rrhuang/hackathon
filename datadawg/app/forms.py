from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import Transaction

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, help_text='First Name')
    last_name = forms.CharField(max_length=50, help_text = 'Last Name')
    email = forms.EmailField(max_length=100, help_text='Enter a valid email address.')
    face_picture = forms.FileField(label='Select a file', help_text='max. 4 megabytes')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'face_picture', 'password1', 'password2')

class SendMoneyForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=User.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

