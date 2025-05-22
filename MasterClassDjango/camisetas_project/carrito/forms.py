from django import forms

class AgregarProductoForm(forms.Form):
    """Formulario para agregar productos al carrito"""
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 1})
    )
    actualizar = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
