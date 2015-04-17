from django.db import models
from empresas.models import Empresa, Sistema, Pessoa

# = models.CharField(max_length=50, blank=True, null=True)
# = models.CharField(max_length=150, blank=True, null=False)
# = models.CharField(max_length=250, blank=True, null=True)

class Cheque(models.Model):
    banco = models.CharField(max_length=50, blank=True, null=True)
    agencia = models.CharField(max_length=50, blank=True, null=True)
    numero_cheque = models.CharField(max_length=50, blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    nome = models.CharField(max_length=150, blank=True, null=True)
    data_recebido = models.DateField(auto_now=False, auto_now_add=False)
    data_compensar = models.DateField(auto_now=False, auto_now_add=False)
    data_compensado = models.DateField(auto_now=False, auto_now_add=False)
    tags = models.CharField(max_length=250, blank=True, null=True)
    empresa = models.ForeignKey(Empresa,related_name="cheque_empresa_id")

class Caixa(models.Model):
    pessoa = models.ForeignKey(Pessoa,related_name="caixa_pessoa_id")
    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)
    data_pagamento = models.DateField(auto_now=False, auto_now_add=False)
    valor_bruto = models.DecimalField(max_digits=7, decimal_places=2)
    valor_multa = models.DecimalField(max_digits=7, decimal_places=2)
    valor_juros = models.DecimalField(max_digits=7, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=7, decimal_places=2) 
    descricao = models.CharField(max_length=250, blank=True, null=True)
    operacao = models.CharField(max_length=250, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
    ativo = models.CharField(default="SIM", max_length=50, blank=False)
    usuario = models.ForeignKey(Pessoa,related_name="caixa_usuario_id")
    empresa = models.ForeignKey(Empresa,related_name="caixa_empresa_id")
    observacao = models.CharField(max_length=250, blank=True, null=True)
    tags = models.CharField(max_length=250, blank=True, null=True)
    data_boleto = models.DateField(auto_now=False, auto_now_add=False)
    processo = models.CharField(max_length=250, blank=True, null=True)
    categoria = models.ForeignKey(Sistema,related_name="caixa_categoria_id")
    grupo = models.ForeignKey(Sistema,related_name="caixa_grupo_id")
    subgrupo = models.ForeignKey(Sistema,related_name="caixa_subgrupo_id")  
    tipo = models.CharField(default="E",max_length=1,blank=False) 
 


class Vinculo(models.Model):
    caixa_pai = models.ForeignKey(Caixa,related_name="vinculo_caixa_pai_id")
    caixa_filho = models.ForeignKey(Caixa,related_name="vinculo_caixa_filho_id")
    observacao = models.CharField(max_length=250, blank=True, null=True)
    rastreador = models.CharField(max_length=250, blank=True, null=True)
    tags = models.CharField(max_length=250, blank=True, null=True)
    empresa = models.ForeignKey(Empresa,related_name="vinculo_empresa_id")





