from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="home"),
    path('vestimenta', views.vestimenta,name='vestimenta'),
    path('calzado', views.calzado,name='calzado'),
    path('accesorios', views.accesorios,name='accesorios'),
    path('suplementos', views.suplementos,name='suplementos'),
    path('contacto/',views.contacto, name="contacto"),
]