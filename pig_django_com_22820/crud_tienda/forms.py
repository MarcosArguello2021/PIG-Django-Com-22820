from django import forms

class FormContacto(forms.Form):
    nombre = forms.CharField(required=False)
    mail = forms.EmailField()
    mensaje = forms.CharField()