# from django.template import loader
from django.shortcuts import render, redirect
from crud_tienda.models import Item
from crud_tienda.forms import FormContacto
from django.core.mail import EmailMessage
from pig_django_com_22820.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    """ esto es la explicación"""
    productos = Item.objects.all()
    return render(request, "crud_tienda/index.html", {"productos": productos})


def calzado(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
    else:
        categoria = "Calzado"
        productos = Item.objects.filter(categoria__icontains="CA").order_by('nombre')
    return render(request, "crud_tienda/calzado.html", {"productos": productos, "categoria": categoria})


def vestimenta(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
        
    else:
        categoria = "Vestimenta"
        productos = Item.objects.filter(categoria__icontains="VM").order_by('nombre')
    return render(request, "crud_tienda/vestimenta.html", {"productos": productos, "categoria": categoria})


def accesorios(request):
    acces = "Accesorios.objects.all().order_by('nombre_accesorios')"
    return render(request, "crud_tienda/accesorios.html", {"accesorios": acces})


def suplementos(request):
    suplem = "Suplementos.objects.all().order_by('nombre_suplementos')"
    return render(request, "crud_tienda/suplementos.html", {"suplementos": suplem})


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
            email = EmailMessage(
                "Tienda: Nuevo mensaje",                            # Asunto
                f"De {nombre} <{mail}>\n\nEscribió:\n\n{mensaje}",  # Cuerpo
                EMAIL_HOST_USER,                                    # Email de origen
                # Email donde llega la respuesta
                ['ivandariomunioz@gmail.com'],
                # responder a...
                reply_to=[mail]
            )
            print(email)
            try:
                email.send()
                return redirect('home')
            except:
                # aca habría que crear una excepcion o mensaje de error propio y que continúe
                raise ValueError("Ocurrió un error...")
    else:
        return render(request, "crud_tienda/contacto.html", {"contact": contact})
