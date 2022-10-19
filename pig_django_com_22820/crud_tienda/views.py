from datetime import datetime
from django.shortcuts import render, redirect
from crud_tienda.forms import FormContacto

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
    contact = FormContacto()
    if request.method == 'POST':
        form = FormContacto(request.POST)
        if form.is_valid():
            email = EmailMessage(
                "Tienda: Nuevo mensaje", # Asunto
                f"De {contact.nombre} <{contact.mail}>\n\nEscribió:\n\n{contact.mensaje}",# Cuerpo
                EMAIL_HOST_USER, # Email de origen
                ['ivandariomunioz@gmail.com']# Email de destino
                reply_to=[contact.email]# Email de respuesta
            )
            try:
                email.send()
                return redirect('home')
            except:
                algo
    return render(request, "crud_tienda/contacto.html",{"contact":contact})