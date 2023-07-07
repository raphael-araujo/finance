from django import forms

from .models import Categoria, Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ('apelido', 'banco', 'tipo', 'valor', 'icone')


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('categoria', 'essencial')
