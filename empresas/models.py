# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, User
from cloudinary.models import CloudinaryField

#Campos Varchar
#Pequenos : 50
#Medios   : 150
#Grandes  : 250
class Empresa(models.Model):
	logo = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
	razao_social = models.CharField(db_index=True,max_length=150, blank=False, null=False)
	nome_fantasia = models.CharField(db_index=True,max_length=150, blank=True, null=False)
	cnpj = models.CharField(max_length=50, blank=True, null=True)
	num_registro = models.CharField(max_length=150, blank=True, null=False)
	endereco_rua = models.CharField(max_length=250, blank=True, null=True)
	endereco_numero = models.CharField(max_length=250, blank=True, null=True)
	endereco_complemento = models.CharField(max_length=250, blank=True, null=True)
	endereco_bairro = models.CharField(max_length=250, blank=True, null=True)
	endereco_cidade = models.CharField(max_length=250, blank=True, null=True)
	endereco_estado = models.CharField(max_length=250, blank=True, null=True)
	endereco_pais = models.CharField(max_length=250, blank=True, null=True)
	endereco_cep = models.CharField(max_length=250, blank=True, null=True)
	telefone_contato = models.CharField(max_length=50, blank=True, null=True)
	telefone_financeiro = models.CharField(max_length=50, blank=True, null=True)
	email_contato = models.CharField(max_length=150, blank=False, null=False)
	email_financeiro = models.CharField(max_length=150, blank=True, null=True)
	facebook = models.CharField(max_length=150, blank=True, null=True)
	googleplus = models.CharField(max_length=150, blank=True, null=True)
	twitter = models.CharField(max_length=150, blank=True, null=True)
	skype = models.CharField(max_length=150, blank=True, null=True)
	conta_banco = models.CharField(max_length=50, blank=True, null=True)
	conta_agencia = models.CharField(max_length=50, blank=True, null=True)
	conta_corrente = models.CharField(max_length=50, blank=True, null=True)
	conta_carteira = models.CharField(max_length=50, blank=True, null=True)
	conta_codigo_cedente = models.CharField(max_length=50, blank=True, null=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	tags = models.CharField(max_length=250, blank=True, null=True)
	ativo = models.CharField(default="SIM", max_length=50, blank=False, null=False)


class Usuario(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
	cpf = models.CharField(_(u'CPF'), max_length=50, blank=True, null=True)
	rg = models.CharField(_(u'RG'), max_length=50, blank=True, null=True)
	facebook = models.CharField(_(u'Facebook'), max_length=150, blank=True, null=True)
	googleplus = models.CharField(_(u'Google Plus'), max_length=150, blank=True, null=True)
	twitter = models.CharField(_(u'Twitter'), max_length=150, blank=True, null=True)
	skype = models.CharField(_(u'Skype'), max_length=150, blank=True, null=True)
	telefone_fixo = models.CharField(_(u'Telefone Fixo'), max_length=50, blank=True, null=True)
	telefone_celular = models.CharField(_(u'Telefone Celular'), max_length=50, blank=True, null=True)
	foto = CloudinaryField(_(u'foto'), blank=True, null=True)
	idioma = models.CharField(_(u'Idioma'), max_length=50, blank=True, null=False)
	empresa = models.ForeignKey(Empresa, related_name="usuario_empresa_id", null=True)

	class Meta:
		verbose_name = _(u'Usuário')
		verbose_name_plural = _(u'Usuários')
		ordering = ['first_name']

	def __unicode__(self):
		return u'{username} ({email})'.format(username=self.username, email=self.email)

class Pessoa(models.Model):
	tipo = models.CharField(max_length=50, blank=True, null=True)
	nome = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	cpf = models.CharField(max_length=50, blank=True, null=True)
	rg = models.CharField(max_length=50, blank=True, null=True)
	conta_banco = models.CharField(max_length=50, blank=True, null=True)
	conta_corrente = models.CharField(max_length=50, blank=True, null=True)
	conta_agencia = models.CharField(max_length=50, blank=True, null=True)
	endereco_rua = models.CharField(max_length=250, blank=True, null=True)
	endereco_numero = models.CharField(max_length=50, blank=True, null=True)
	endereco_complemento = models.CharField(max_length=250, blank=True, null=True)
	endereco_bairro = models.CharField(max_length=250, blank=True, null=True)
	endereco_cidade = models.CharField(max_length=250, blank=True, null=True)
	endereco_estado = models.CharField(max_length=250, blank=True, null=True)
	endereco_pais = models.CharField(max_length=250, blank=True, null=True)
	endereco_cep = models.CharField(max_length=50, blank=True, null=True)
	telefone_fixo = models.CharField(max_length=50, blank=True, null=True)
	telefone_celular = models.CharField(max_length=50, blank=True, null=True)
	email_pessoal = models.CharField(max_length=250, blank=True, null=True)
	email_empresarial = models.CharField(max_length=250, blank=True, null=True)
	facebook = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	googleplus = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	skype = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	twitter = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	empresa = models.ForeignKey(Empresa,related_name="pessoa_empresa_id")
	usuario = models.ForeignKey(Usuario,related_name="pessoa_usuario_id")
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	ativo = models.CharField(default="SIM", max_length=50, blank=False, null=False)
	anotacacoes = models.CharField(max_length=250, blank=True, null=True)
	grupo_pessoa = models.CharField(db_index=True,max_length=150, blank=True, null=False) 
	tags = models.CharField(max_length=250, blank=True, null=True)


