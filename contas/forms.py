from django import forms
from contas.models import Caixa, Vinculo, Sistema, Cheque

class CaixaForm(forms.ModelForm):

    class Meta:
        model = Caixa

class VinculoForm(forms.ModelForm):

    class Meta:
        model = Vinculo

class SistemaForm(forms.ModelForm):

    class Meta:
        model = Sistema

class ChequeForm(forms.ModelForm):

    class Meta:
        model = Cheque