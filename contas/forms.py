from django import forms
from contas.models import Caixa, Vinculo, Cheque

class CaixaForm(forms.ModelForm):

    class Meta:
        model = Caixa

class VinculoForm(forms.ModelForm):

    class Meta:
        model = Vinculo

class ChequeForm(forms.ModelForm):

    class Meta:
        model = Cheque