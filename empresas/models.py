from django.db import models

class Empresa(models.Model):
	logo = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
	razao_social = models.CharField(max_lenght=100, blank=False, null=False)
	nome_fantasia = models.CharField(max_lenght=100, blank=False, null=False)
	cnpj = models.CharField(db_index=True, max_length=18, blank=True, null=True)
	endereco = models.CharField(max_lenght=100, blank=False, null=False)
	telefone = models.CharField(max_lenght=15, blank=False, null=False)

class Usuario(models.Model):
