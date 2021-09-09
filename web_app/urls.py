from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('create_account', views.create_account, name='create_account'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
