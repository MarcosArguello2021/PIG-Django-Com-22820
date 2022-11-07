from django.contrib import admin
from .models import Vestimenta, Calzado, Suplemento, Accesorio

# Register your models here.
class VestimentaAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","foto","info","stock","categoria","sexo","talle") # campos q aparecen
    fields = ['nombre','foto','stock','precio',('categoria','sexo','talle', 'subcategoria'),'info'] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
    search_fields = ('nombre',)
    list_filter = ("precio","categoria","sexo","stock", "talle")


# class ClazadoAdmin(admin.ModelAdmin):
#     list_display = ("nombre","precio","foto","info","stock","categoria","sexo","talle") # campos q aparecen
#     fields = ['nombre','foto','stock','precio',('categoria','sexo','talle', 'subcategoria'),'info'] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
#     search_fields = ('nombre',)
#     list_filter = ("precio","categoria","sexo","stock", "talle")

admin.site.register(Vestimenta, VestimentaAdmin)
admin.site.register(Calzado)
admin.site.register(Suplemento)
admin.site.register(Accesorio)