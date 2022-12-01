from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registro_usuarios/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='Home'), name="logout"),
]