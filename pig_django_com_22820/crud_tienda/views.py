from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from crud_tienda.models import Vestimenta, Accesorio, Calzado, Suplemento
from crud_tienda.forms import FormContacto
from django.core.mail import EmailMessage
from pig_django_com_22820.settings import EMAIL_HOST_USER

# Create your views here.


class IndexView(TemplateView):
    template_name = "crud_tienda/index.html"
    # model = Vestimenta
    # context_object_name = 'productos' # este es el queryset, no el contexto. CUAL es el contexto?
    # queryset = Vestimenta.objects.all().order_by('?')[:5]
    # productos = Item.objects.all().order_by('?')[:10]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['vestimentas'] = self.queryset
        context['vestimentas'] = Vestimenta.objects.all().order_by('?')[:5]
        context['calzados'] = Calzado.objects.all().order_by('?')[:5]
        context['accesorios'] = Accesorio.objects.all().order_by('?')[:5]
        context['suplementos'] = Suplemento.objects.all().order_by('?')[:5]
        print(context) # en produccion se va...
        return context

# class Calzado(ListView):
#     model = Calzado
#     context_object_name = 'productos' # este es el queryset
#     template_name = "crud_tienda/calzado.html"
#     queryset = Calzado.objects.all().order_by('nombre')

#     def get(self, request, *args, **kwargs):
#         dict = request.GET
#         print(dict)
#         if dict['filtro'] == 'M' or dict['filtro'] == 'H':
#             productos = Calzado.objects.filter(sexo=dict['filtro']).order_by('nombre')
#         elif dict['filtro'] != None:
#             productos = Calzado.objects.filter(talle=dict['filtro']).order_by('nombre')
#         else:
#             productos = Calzado.objects.all().order_by('nombre')
#         return render(request,self.template_name,{"productos":productos})



def calzado(request):
    categoria = "Calzado"
    talles = (
    ('34.5'),
    ('35.5'),
    ('36'),
    ('38'),
    ('39'),
    ('40'),
    ('41'),
    ('41.5'),
    ('42'),
    ('43'),
    ('44'),
    ('45'),
    )

    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
    else:
        dict = request.GET
        print("--------------")
        print(dict)
        print("--------------")
        if dict:
            if dict['filtro'] == 'M' or dict['filtro'] == 'H':
                productos = Calzado.objects.filter(sexo=dict['filtro']).order_by('nombre')
            elif dict['filtro'] != None:
                productos = Calzado.objects.filter(talle=dict['filtro']).order_by('nombre')
        else:
            productos = Calzado.objects.all().order_by('nombre')
    return render(request, "crud_tienda/calzado.html", {"productos": productos, "categoria": categoria,"talles":talles})


def vestimenta(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        talle = request.POST['talle']
        
    else:
        categoria = "Vestimenta"
        productos = Vestimenta.objects.filter(categoria__icontains="VM").order_by('nombre')
    return render(request, "crud_tienda/vestimenta.html", {"productos": productos, "categoria": categoria})


def accesorios(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        
    else:
        categoria = "Accesorios"
        productos = Accesorio.objects.filter(categoria__icontains="AC").order_by('nombre')
    return render(request, "crud_tienda/accesorios.html", {"productos": productos, "categoria": categoria})


def suplementos(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
    else:
        categoria = "Sumplementos"
        productos = Suplemento.objects.filter(categoria__icontains="SU").order_by('nombre')
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
