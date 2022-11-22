from django.urls import path, re_path
from crud_tienda.views import IndexView
from . import views
from .views import CalzadoLista, AccesoriosLista, SuplementosLista, VestimentaLista, DetalleAccesorios
from django.conf import settings

urlpatterns = [
    path('', IndexView.as_view() ,name="Home"),
    path('vestimenta/', VestimentaLista.as_view(),name='Vestimenta'),
    path('vestimenta/<str:filtro>/', VestimentaLista.as_view(),name='Vestimenta-filtro'),
    # path('vestimenta/', views.vestimenta,name='Vestimenta'),
    path('calzado/', CalzadoLista.as_view(),name='Calzado'),
    path('calzado/<str:filtro>/', CalzadoLista.as_view(),name='Calzado-filtro'),
    # path('calzado/', views.calzado,name='Calzado'),
    # path('calzado/<str:filtro>/', views.calzado,name='Calzado-filtro'),
    # re_path(r'^calzado/(?P<sexo>[a-z]{,1})$', views.calzado,name='calzado-sexo'),
    # path('accesorios/', views.accesorios,name='Accesorios'),
    path('accesorios/', AccesoriosLista.as_view(),name='Accesorios'),
    path('accesorios/<str:filtro>/', AccesoriosLista.as_view(),name='Accesorios-filtro'),
    path('suplementos/', SuplementosLista.as_view(),name='Suplementos'),
    path('suplementos/<str:filtro>/', SuplementosLista.as_view(),name='Suplementos-filtro'),
    path('detalle/<int:pk>', DetalleAccesorios.as_view(), name="detalle"), 
    # path('suplementos/', views.suplementos,name='Suplementos'),
    path('contacto/',views.contacto, name="Contacto"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)