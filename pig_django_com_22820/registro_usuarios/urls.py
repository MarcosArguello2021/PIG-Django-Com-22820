from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registro_usuarios/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='Home'), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registro_usuarios/password_reset_form.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registro_usuarios/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registro_usuarios/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registro_usuarios/password_reset_complete.html'), name="password_reset_complete"),
]