from datetime import datetime
from django.shortcuts import render, redirect
from crud_tienda.forms import FormContacto
from django.core.mail import send_mail, EmailMessage
from pig_django_com_22820.settings import EMAIL_HOST_USER

# Create your views here.
def index(request):
    """ esto es la explicacion"""
    fecha=datetime.now().strftime("%D - %H:%M:%S")
    return render(request, "crud_tienda/index.html",{"fecha_now":fecha})

def vestimenta(request):
    ropa="Ropa.objects.all().order_by('nombre_ropa')"
    return render(request,"crud_tienda/vestimenta.html",{"ropa":ropa})

def calzado(request):
    zapas="Calzado.objects.all().order_by('nombre_calzado')"
    return render(request,"crud_tienda/calzado.html",{"calzado":zapas})

def accesorios(request):
    acces="Accesorios.objects.all().order_by('nombre_accesorios')"
    return render(request,"crud_tienda/accesorios.html",{"accesorios":acces})

def suplementos(request):
    suplem="Suplementos.objects.all().order_by('nombre_suplementos')"
    return render(request,"crud_tienda/suplementos.html",{"suplementos":suplem})


def contacto(request):
    """formulario de contacto"""
    contact = FormContacto()
    if request.method == 'POST':
        contact = FormContacto(request.POST)
        nombre = request.POST['nombre']
        mail = request.POST['mail']
        mensaje = request.POST['mensaje']
        if contact.is_valid():
            # enviamos el email
            # email = EmailMessage(
            #     "Tienda: Nuevo mensaje",                                                        # Asunto
            #     f"De {nombre} <{mail}>\n\nEscribió:\n\n{mensaje}",      # Cuerpo
            #     mail,                                                                   # Email de origen, from  (default = EMAIL_HOST_USER,)
            #     ['ivandariomunioz@gmail.com'],                                                  # Email de destino, to
            #     reply_to=[mail]                                                                # Email de respuesta
            # )
            # print(email)
            # try:
            #     email.send()
            #     return redirect('home')
            # except:
            #     raise ValueError("Ocurrió un error...")
            return redirect('home') # POR AHORA SOLOS REDIRIGIMOS
    else:
        return render(request, "crud_tienda/contacto.html",{"contact":contact})