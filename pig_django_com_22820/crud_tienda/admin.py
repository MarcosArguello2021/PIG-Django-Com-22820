from django.contrib import admin
from .models import Vestimenta, Calzado, Suplemento, Accesorio

# Register your models here.
class VestimentaAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","foto","info","stock","sexo","talle") # campos q aparecen
    fields = ['nombre','foto','stock','precio',('sexo','talle', 'subcategoria'),'info'] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
    search_fields = ('nombre',)
    list_filter = ("precio","sexo","stock", "talle")


class CalzadoAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","foto","info","stock","sexo","talle") # campos q aparecen
    fields = ['nombre','foto','stock','precio',('sexo','talle'),'info'] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
    search_fields = ('nombre',)
    list_filter = ("precio","sexo","stock", "talle")

admin.site.register(Vestimenta, VestimentaAdmin)
admin.site.register(Calzado, CalzadoAdmin)
admin.site.register(Suplemento)
admin.site.register(Accesorio)