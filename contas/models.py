from django.db import models

# = models.CharField(max_length=50, blank=True, null=True)
# = models.CharField(max_length=150, blank=True, null=False)
# = models.CharField(max_length=250, blank=True, null=True)

class Caixa(models.Model):
	pessoa_id = models.ForeignKey(Pessoa,related_name="pessoa_id")
	valor_bruto = models.DecimalField(max_digits=7, decimal_places=2)
	data_vencimento = models.DateTimeField(auto_now=False, auto_now_add=False)
	data_pagamento = models.DateTimeField(auto_now=False, auto_now_add=False)
	valor_multa = models.DecimalField(max_digits=7, decimal_places=2)
	valor_juros = models.DecimalField(max_digits=7, decimal_places=2)
	valor_desconto = models.DecimalField(max_digits=7, decimal_places=2) 
	descricao = models.CharField(max_length=250, blank=True, null=True)
	operacao = models.CharField(max_length=250, blank=True, null=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	ativo = models.CharField(default="SIM", max_length=50, blank=False, null=False)
	usuario_id = models.ForeignKey(Pessoa,related_name="pessoa_id")
	empresa_id = models.ForeignKey(Empresa,related_name="empresa_id")
	observacao = models.CharField(max_length=250, blank=True, null=True)
	tags = models.CharField(max_length=250, blank=True, null=True)
	data_boleto = models.DateTimeField(auto_now=False, auto_now_add=False)
	processo = models.CharField(max_length=250, blank=True, null=True)
	categoria_id = models.ForeignKey(Sistema,related_name="categoria_id")
	grupo_id = models.ForeignKey(Sistema,related_name="grupo_id")
	subgrupo_id = models.ForeignKey(Sistema,related_name="subgrupo_id")


#class Vinculo(models.Model):

