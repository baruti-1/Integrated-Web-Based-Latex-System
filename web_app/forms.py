from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your preferred username'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your first name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your last name'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter strong password'})
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username already registered')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already registered')
        return email