from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","foto","info","stock","categoria","sexo") # campos q aparecen (falta talle)
    fields = ['nombre','foto','stock','precio',('categoria','sexo', 'subcategoria'),'info'] # orden (si los meto en una tupla (a,b,c) los muestra en horizontal)
    search_fields = ('nombre',)
    list_filter = ("precio","categoria","sexo","stock")

admin.site.register(Item, ItemAdmin)