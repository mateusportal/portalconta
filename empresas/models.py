# coding: utf-8
from django.db import models

#Campos Varchar
#Pequenos : 50
#Medios   : 150
#Grandes  : 250
class Empresa(models.Model):
	logo = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
	razao_social = models.CharField(db_index=True,max_lenght=150, blank=False, null=False)
	nome_fantasia = models.CharField(db_index=True,max_lenght=150, blank=True, null=False)
	cnpj = models.CharField(max_length=50, blank=True, null=True)
	num_registro = models.CharField(max_lenght=150, blank=True, null=False)
	endereco_rua = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_numero = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_complemento = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_bairro = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_cidade = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_estado = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_pais = models.CharField(max_lenght=250, blank=True, null=True)
	endereco_cep = models.CharField(max_lenght=250, blank=True, null=True)
	telefone_contato = models.CharField(max_lenght=50, blank=True, null=True)
	telefone_financeiro = models.CharField(max_lenght=50, blank=True, null=True)
	email_contato = models.CharField(max_lenght=150, blank=False, null=False)
	email_financeiro = models.CharField(max_lenght=150, blank=True, null=True)
	facebook = models.CharField(max_lenght=150, blank=True, null=True)
	googleplus = models.CharField(max_lenght=150, blank=True, null=True)
	twitter = models.CharField(max_lenght=150, blank=True, null=True)
	skype = models.CharField(max_lenght=150, blank=True, null=True)
	conta_banco = models.CharField(max_lenght=50, blank=True, null=True)
	conta_agencia = models.CharField(max_lenght=50, blank=True, null=True)
	conta_corrente = models.CharField(max_lenght=50, blank=True, null=True)
	conta_carteira = models.CharField(max_lenght=50, blank=True, null=True)
	conta_codigo_cedente = models.CharField(max_lenght=50, blank=True, null=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	tags = models.CharField(max_lenght=250, blank=True, null=True)
	ativo = models.CharField(default="SIM" max_lenght=50, blank=False, null=False)

class Usuario(models.Model):
