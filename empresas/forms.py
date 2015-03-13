from django import forms
from empresas.models import Pessoa, Empresa

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
