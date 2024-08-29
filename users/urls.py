from django.urls import path   #3
from .import views   #3
from django.contrib.auth import views as auth_view   #4

urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),   #3
    path('profile/', views.profile, name='users-profile'),   #3
    path('', auth_view.LoginView.as_view(template_name='users/login.html'),   #4
         name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),
         name='users-logout'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),  #4
         name='password_reset_complete'),
]