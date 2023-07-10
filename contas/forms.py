from django import forms

from .models import ContaPagar


class ContaPagarForm(forms.ModelForm):
    dia_de_pagamento = forms.IntegerField(min_value=1, max_value=31)
    
    class Meta:
        model = ContaPagar
        fields = '__all__'
