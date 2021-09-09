from django.urls import path
from user_account import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_change', PasswordChangeView.as_view(template_name='user_account/change_password.html'), name='change_password'),
    path('password_change_done', PasswordChangeDoneView.as_view(template_name='user_account/password_change_done.html'), name='password_change_done'),
    path("profile", views.profile, name="profile"), 
    path('templates', views.templates, name='templates'),
    path('template/<int:tmp_id>', views.template, name='template'),
    path('report', views.report, name='report'),
    # path('report', views.compile, name='compile'),
    path('user_templates', views.user_templates, name='user_templates'),
    path('download/', views.report_download, name='report_download')
] 