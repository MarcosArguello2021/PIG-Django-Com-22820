from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index ,name="home"),
    path('vestimenta', views.vestimenta,name='vestimenta'),
    path('calzado', views.calzado,name='calzado'),
    path('accesorios', views.accesorios,name='accesorios'),
    path('suplementos', views.suplementos,name='suplementos'),
    path('contacto/',views.contacto, name="contacto"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)