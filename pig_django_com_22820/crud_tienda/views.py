from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from crud_tienda.models import Vestimenta, Accesorio, Calzado, Suplemento, Opciones_calzado, Opciones_vestimenta, SEXO
from crud_tienda.forms import FormContacto, VestimentaForm, CalzadoForm
from django.core.mail import EmailMessage
from pig_django_com_22820.settings import EMAIL_HOST_USER
from itertools import chain
# Create your views here.

def pasar_a_dict(tuplaChoices):
        llaves = []
        for e in tuplaChoices:
            llaves.append(e[0])
        valores = []
        for e in tuplaChoices:
            valores.append(e[1])
        dict = {}
        for i in range(len(valores)):
            dict[llaves[i]]=valores[i]
        # print(dict)
        return dict

class IndexView(TemplateView):
    template_name = "crud_tienda/index.html"
    # model = Vestimenta
    # context_object_name = 'productos' # este es el queryset, no el contexto. CUAL es el contexto?
    # queryset = Vestimenta.objects.all().order_by('?')[:5]
    # productos = Item.objects.all().order_by('?')[:10]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['vestimentas'] = self.queryset
        vestimentas = Vestimenta.objects.all().order_by('?')[:5]
        calzados = Calzado.objects.all().order_by('?')[:5]
        accesorios = Accesorio.objects.all().order_by('?')[:5]
        suplementos = Suplemento.objects.all().order_by('?')[:5]
        queryList = list(chain(vestimentas, calzados, accesorios, suplementos))
        context['object_list'] = queryList
        print(context)  # en produccion se va...
        return context


class CalzadoLista(ListView):
    model = Calzado
    template_name = "crud_tienda/calzado.html"
    sexo = pasar_a_dict(SEXO)
    talles = pasar_a_dict(Opciones_calzado.TALLES)
    
    def get(self, request, *args, **kwargs):
        dict = request.GET
        print(dict)
        if dict:
            if dict['filtro'] in self.sexo.keys():
                object_list = Calzado.objects.filter(sexo=dict['filtro']).order_by('nombre')
            elif dict['filtro'] in self.talles.keys():
                object_list = Calzado.objects.filter(opciones_calzado__talle=str(dict['filtro']))
        else:
            object_list = Calzado.objects.all().order_by('nombre')
        return render(request, self.template_name, {"object_list": object_list, "sexo":self.sexo, "talles": self.talles})


class VestimentaLista(ListView):
    model = Vestimenta
    template_name = 'crud_tienda/vestimenta.html'
    sexo = pasar_a_dict(SEXO)
    subcat_dict = pasar_a_dict(Vestimenta.SUBCATEGORIA)
    talles = pasar_a_dict(Opciones_vestimenta.TALLES)

    # talles = []
    # for tuplita in Opciones_vestimenta.TALLES:
    #     talles.append(tuplita[0])

    # subcat = []
    # for subc in Vestimenta.SUBCATEGORIA:
    #     subcat.append(subc[0])
    # subcat_val = []
    # for subc in Vestimenta.SUBCATEGORIA:
    #     subcat_val.append(subc[1])
    # subcat_dict = {}
    # for i in range(len(subcat_val)):
    #     subcat_dict[subcat[i]]=subcat_val[i]
    # print(subcat_dict)

    def get(self, request, *args, **kwargs):
        dict = request.GET
        print('-----------')
        print(dict)
        print('-----------')
        if dict:
            if dict['filtro'] in self.sexo.keys():
                object_list = Vestimenta.objects.filter(sexo=dict['filtro']).order_by('nombre')
            elif dict['filtro'] in self.subcat_dict.keys():
                object_list = Vestimenta.objects.filter(subcategoria=str(dict['filtro']))
            elif dict['filtro'] in self.talles.keys():
                object_list = Vestimenta.objects.filter(opciones_vestimenta__talle=str(dict['filtro']))
        else:
            object_list = Vestimenta.objects.all().order_by('nombre')
        return render(request, self.template_name, {"object_list": object_list, "sexo":self.sexo, "talles": self.talles,"subcat_dict":self.subcat_dict})

class VestimentaCreate(CreateView):
    model = Vestimenta
    form_class = VestimentaForm
    template_name = 'administrador/crear_vestimenta.html'
    success_url = reverse_lazy('Home')

    # def get_context_data(self, **kwargs):
    #     data = super(VestimentaCreate, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['files'] = VestimentaForm(self.request.POST, self.request.FILES)
    #     else:
    #         data['files'] = VestimentaForm()
    #     return data


    # def get(self, request, *args, **kwargs):
    #     # form = self.form_class()
    #     return reverse_lazy(self.template_name,{'form_class':self.form_class}) #{'form_class':form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return super().post(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse_lazy('Home')



class AccesoriosLista(ListView):
    model = Accesorio
    template_name = 'crud_tienda/accesorios.html'
    subcat_dict = pasar_a_dict(Accesorio.SUBCATEGORIA)

    def get(self, request, *args, **kwargs):
        dict = request.GET
        print('-----------')
        print(dict)
        print('-----------')
        if dict:
            if dict['filtro'] in self.subcat_dict.keys():
                object_list = Accesorio.objects.filter(subcategoria=str(dict['filtro']))
        else:
            object_list = Accesorio.objects.all().order_by('nombre')
        return render(request, self.template_name, {"object_list": object_list, "subcat_dict":self.subcat_dict})



class SuplementosLista(ListView):
    model = Suplemento
    template_name = 'crud_tienda/suplementos.html'
    subcat_dict = pasar_a_dict(Suplemento.SUBCATEGORIA)

    def get(self, request, *args, **kwargs):
        dict = request.GET
        print('-----------')
        print(dict)
        print('-----------')
        if dict:
            if dict['filtro'] in self.subcat_dict.keys():
                object_list = Suplemento.objects.filter(subcategoria=str(dict['filtro']))
        else:
            object_list = Suplemento.objects.all().order_by('nombre')
        return render(request, self.template_name, {"object_list": object_list, "subcat_dict":self.subcat_dict})


class AccesoriosDetalle(DetailView):
    model = Accesorio
    template_name = 'crud_tienda/detalle.html'

class CalzadoDetalle(DetailView):
    model = Calzado
    template_name = 'crud_tienda/detalle.html'

class SuplementosDetalle(DetailView):
    model = Suplemento
    template_name = 'crud_tienda/detalle.html'

class VestimentaDetalle(DetailView):
    model = Vestimenta
    template_name = 'crud_tienda/detalle.html'




# Vistas basadas en funciones:

# def calzado(request):
#     talles = (
#     ('34.5'),
#     ('35.5'),
#     ('36'),
#     ('38'),
#     ('39'),
#     ('40'),
#     ('41'),
#     ('41.5'),
#     ('42'),
#     ('43'),
#     ('44'),
#     ('45'),
#     )

#     if request.method == 'POST':
#         talle = request.POST['talle']
#     else:
#         dict = request.GET
#         print("--------------")
#         print(dict)
#         print("--------------")
#         if dict:
#             if dict['filtro'] == 'M' or dict['filtro'] == 'H':
#                 object_list = Calzado.objects.filter(sexo=dict['filtro']).order_by('nombre')
#             elif dict['filtro'] != None:
#                 object_list = Calzado.objects.filter(opciones_calzado__talle=str(dict['filtro']))
#         else:
#             object_list = Calzado.objects.all().order_by('nombre')
#     return render(request, "crud_tienda/calzado.html", {"object_list": object_list,"talles":talles})



# def vestimenta(request):
#     if request.method == 'POST':
#         categoria = request.POST['categoria']
#         talle = request.POST['talle']
#     else:
#         productos = Vestimenta.objects.all().order_by('nombre')
#     return render(request, "crud_tienda/vestimenta.html", {"productos": productos})


# def accesorios(request):
#     if request.method == 'POST':
#         categoria = request.POST['categoria']
#     else:
#         productos = Accesorio.objects.all().order_by('nombre')
#     return render(request, "crud_tienda/accesorios.html", {"productos": productos})


# def suplementos(request):
#     if request.method == 'POST':
#         categoria = request.POST['categoria']
#     else:
#         categoria = "Sumplementos"
#         productos = Suplemento.objects.all().order_by('nombre')
#     return render(request, "crud_tienda/suplementos.html", {"productos": productos, "categoria": categoria})


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
                return redirect('Home')
            except:
                # aca habría que crear una excepcion o mensaje de error propio y que continúe
                raise ValueError("Ocurrió un error...")
    else:
        return render(request, "crud_tienda/contacto.html", {"contact": contact})
