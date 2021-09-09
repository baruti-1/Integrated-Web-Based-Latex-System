from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {'first_name': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
                    'last_name': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'}),
                    'email': forms.TextInput(attrs={'class':'form-control mt-2 mb-2'})}

        
