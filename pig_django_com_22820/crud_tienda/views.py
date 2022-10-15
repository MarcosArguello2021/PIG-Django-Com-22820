from datetime import datetime
from django.shortcuts import render
from crud_tienda.forms import FormContacto

# Create your views here.
def index(request):
    """ esto es la explicacion"""
    fecha=datetime.now().strftime("%D - %H:%M:%S")
    return render(request, "crud_tienda/index.html",{"fecha_now":fecha})

def contacto(request):
    contacto = FormContacto()
    return render(request, "crud_tienda/contacto.html",{"contact":contacto})