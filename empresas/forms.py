from django import forms
from empresas.models import Usuario, Pessoa, Empresa

class LoginForm(forms.Form):
    username = forms.CharField(max_length='200', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
