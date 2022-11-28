from django import forms
from .models import Calzado, Vestimenta, Suplemento, Accesorio, Opciones_calzado, Opciones_vestimenta


class FormContacto(forms.Form):
    nombre = forms.CharField(required=False)
    mail = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'size':'10'}))


class FormCalzado(forms.ModelForm):
    
    class Meta:
        model = Calzado
        second_model = Opciones_calzado
        fields = ('nombre','precio','foto','info') #,'sexo','talle','stock') #exclude = 'calzado'

class FormVestimenta(forms.ModelForm):

    class Meta:
        model = Vestimenta
        exclude = ('categoria',)