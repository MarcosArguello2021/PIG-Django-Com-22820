# from django.template import loader
from django.shortcuts import render, redirect
from crud_tienda.models import Item
from crud_tienda.forms import FormContacto
from django.core.mail import EmailMessage
from pig_django_com_22820.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    """ esto es la explicación"""
    productos = Item.objects.all().order_by('?')[:10]
    return render(request, "crud_tienda/index.html", {"productos": productos})


def calzado(request,filtro=None):
    categoria = "Calzado"
    talle = (
    ('34.5(3.5 uk)'),
    ('35.5(4 uk)'),
    ('36(4.5 uk)'),
    ('38(6 uk)'),
    ('39(7 uk)'),
    ('40(8 uk)'),
    ('41(8.5 uk)'),
    ('41.5(9 uk)'),
    ('42(9.5 uk)'),
    ('43(10 uk)'),
    ('44(11 uk)'),
    ('45(11.5 uk)'),
    )
    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
    elif request.method == 'GET':
        filtro = request.GET
        print(request.GET)
        if filtro == 'M' or filtro == 'H':
            productos = Item.objects.filter(categoria__contains="CA",sexo=filtro).order_by('nombre')
        elif
        if filtro == 'Mujer':
            productos = Item.objects.filter(categoria__contains="CA",sexo='M').order_by('nombre')
        elif filtro == 'Hombre':
            productos = Item.objects.filter(categoria__contains="CA",sexo='H').order_by('nombre')
        elif filtro == request.GET:
            print(filtro)
        else:
            productos = Item.objects.filter(categoria__contains="CA").order_by('nombre')
    return render(request, "crud_tienda/calzado.html", {"productos": productos, "categoria": categoria,"talle":talle,"filtro":filtro})


def vestimenta(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
        
    else:
        categoria = "Vestimenta"
        productos = Item.objects.filter(categoria__icontains="VM").order_by('nombre')
    return render(request, "crud_tienda/vestimenta.html", {"productos": productos, "categoria": categoria})


def accesorios(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        
    else:
        categoria = "Accesorios"
        productos = Item.objects.filter(categoria__icontains="AC").order_by('nombre')
    return render(request, "crud_tienda/accesorios.html", {"productos": productos, "categoria": categoria})


def suplementos(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
    else:
        categoria = "Sumplementos"
        productos = Item.objects.filter(categoria__icontains="SU").order_by('nombre')
    return render(request, "crud_tienda/suplementos.html", {"productos": productos, "categoria": categoria})


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
