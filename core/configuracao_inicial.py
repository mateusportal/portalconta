# coding: utf-8
from empresas.models import Sistema
from django.utils.translation import ugettext as _

def configuracao_inicial(id_empresa):
	sistema = Sistema()
	sistema.tipo = _(u'TIPO PESSOA')
	sistema.nome = _(u'CLIENTE')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'TIPO PESSOA')
	sistema.nome = _(u'FORNECEDOR')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'TIPO PESSOA')
	sistema.nome = _(u'FUNCIONÁRIO(A)')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'CATEGORIA')
	sistema.nome = _(u'CAIXA INTERNO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'CATEGORIA')
	sistema.nome = _(u'CAIXA EXTERNO BANCO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'GRUPO')
	sistema.nome = _(u'PRODUTOS E SERVIÇOS')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'GRUPO')
	sistema.nome = _(u'ADMINISTRATIVO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'GRUPO')
	sistema.nome = _(u'FINANCEIRO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'MANUTENÇÃO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'OUTROS')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'HONORÁRIOS')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'ADIANTAMENTO')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'OUTROS')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'TELEFONIA')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
	sistema = Sistema()
	sistema.tipo = _(u'SUB-GRUPO')
	sistema.nome = _(u'TAXAS')
	sistema.empresa_id = id_empresa
	sistema.tags = 'PADRÃO '
	sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
	sistema.save()
