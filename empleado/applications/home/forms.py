from django import forms
from .models import Prueba_DB

class PruebaForm(forms.ModelForm):
    """Form definition fo Prueba."""

    class Meta:
        model = Prueba_DB
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Escriba el titulo',
                }
            ),
            'subtitulo': forms.TextInput(
                attrs={
                    'placeholder': 'Escriba el subtitulo'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder': 'Escriba la cantidad'
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        if cantidad < 1:
            raise forms.ValidationError('Ingrese un numero mayor a 0')
        return cantidad
            