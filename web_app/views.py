from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from . forms import RegisterForm

User = get_user_model()
def create_account(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            return redirect('login')
    else:
         form = RegisterForm()
    context = {'form':form, 'section':'signup'}
    return render(request, 'web_app/create_account.html', context,)

