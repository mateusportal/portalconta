# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index', name='index'),
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^logout/$', 'core.views.logout', name='login'),
    url(r'^valida_login/$', 'core.views.valida_login', name='valida_login'),
    url(r'^cadastro/$', 'core.views.cadastro', name='cadastro'),
    url(r'^valida_cadastro/$', 'core.views.valida_cadastro', name='valida_cadastro'),

    url(r'^sistema/(?P<empresaId>\d+)/$', 'core.views.sistema', name='sistema'),
    url(r'^sistema/calendario/$', 'core.views.calendario', name='calendario'),
    url(r'^sistema/empresa/$', 'core.views.cadastroEmpresa', name='cadastroEmpresa'),  

    url(r'^sistema/caixa/$', 'contas.views.caixa', name='caixa'),
    url(r'^sistema/caixa/formulario/(?P<caixaId>\d+)/$', 'contas.views.caixa_formulario', name='caixa_formulario'),
    url(r'^sistema/caixa/gravar/$', 'contas.views.caixa_gravar', name='caixa_gravar'),
    url(r'^sistema/caixa/excluir/(?P<caixaId>\d+)/$', 'contas.views.caixa_excluir', name='caixa_excluir'),

    url(r'^sistema/pessoas/$', 'empresas.views.pessoas', name='pessoas'),
    url(r'^sistema/pessoas/excluir/(?P<pessoaId>\d+)$', 'empresas.views.pessoas_excluir', name='pessoas_excluir'),
    url(r'^sistema/pessoas/formulario/(?P<pessoaId>\d+)$', 'empresas.views.pessoas_formulario', name='pessoa_formulario'),    
    url(r'^sistema/pessoas/gravar/$', 'empresas.views.pessoas_gravar', name='pessoas_gravar'),
  
    url(r'^sistema/cheque/$', 'contas.views.cheque', name='cheque'),
    url(r'^sistema/cheque/formulario/(?P<chequeId>\d+)$', 'contas.views.cheque_formulario', name='cheque_formulario'),
    url(r'^sistema/cheque/gravar/$', 'contas.views.cheque_gravar', name='cheque_gravar'),
    url(r'^sistema/cheque/excluir/(?P<chequeId>\d+)$', 'contas.views.cheque_excluir', name='cheque_excluir'),

    url(r'^sistema/sistema/$', 'empresas.views.sistema', name='sistema'),
    url(r'^sistema/sistema/formulario/(?P<sisId>\d+)/$', 'empresas.views.sistema_formulario', name='sistema_formulario'),
    url(r'^sistema/sistema/gravar/$', 'empresas.views.sistema_gravar', name='sistema_gravar'),
    url(r'^sistema/sistema/excluir/$', 'empresas.views.sistema_excluir', name='sistema_excluir'),

    url(r'^sistema/usuario/$', 'core.views.usuario', name='usuario'),
    url(r'^sistema/usuario/gravar/$', 'core.views.usuario_gravar', name='usuario_gravar'),

    url(r'^termos-de-uso/$', 'core.views.termos_de_uso', name='termos_de_uso'),
    url(r'^politica-de-privacidade/$', 'core.views.politica_de_privacidade', name='politica_de_privacidade'),
    
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)
