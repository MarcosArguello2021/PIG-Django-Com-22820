from django.urls import path, re_path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index ,name="Home"),
    path('vestimenta/', views.vestimenta,name='Vestimenta'),
    path('calzado/', views.calzado,name='Calzado'),
    path('calzado/<str:sexo>/', views.calzado,name='Calzado-sexo'),
    # re_path(r'^calzado/(?P<sexo>[a-z]{,1})$', views.calzado,name='calzado-sexo'),
    path('accesorios/', views.accesorios,name='Accesorios'),
    path('suplementos/', views.suplementos,name='Suplementos'),
    path('contacto/',views.contacto, name="Contacto"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)