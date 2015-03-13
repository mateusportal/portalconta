from django import forms
from empresas.models import Usuario, Pessoa, Empresa

class LoginForm(forms.Form):
    username = forms.CharField(max_length='200', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UsuarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        self.fields['last_login'].widget = forms.HiddenInput()
        self.fields['date_joined'].widget = forms.HiddenInput()

    class Meta:
        model = Usuario

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
