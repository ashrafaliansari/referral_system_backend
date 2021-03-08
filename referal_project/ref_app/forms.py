from django import forms
from django.forms import ModelForm
from .models import SignUp


class RegisterForm(ModelForm):

    class Meta:
        model = SignUp

        fields=['first_name','last_name','email','username','referral_code','score',
        ]        
        