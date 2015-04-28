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

    url(r'^sistema/$', 'core.views.sistema', name='sistema'),
    url(r'^sistema/calendario/$', 'core.views.calendario', name='calendario'),
    url(r'^sistema/empresa/$', 'core.views.cadastroEmpresa', name='cadastroEmpresa'),  

    url(r'^sistema/caixa/$', 'contas.views.listarCaixa', name='listarCaixa'),
    url(r'^sistema/caixa/editor/$', 'core.views.cadastrarCaixa', name='cadastrarCaixa'),
    url(r'^sistema/caixa/editor/(?P<caixaId>\d+)/$', 'contas.views.preencherCaixa', name='preencherCaixa'),
    url(r'^sistema/caixa/gravar/$', 'contas.views.gravarCaixa', name='gravarCaixa'),
    url(r'^sistema/caixa/excluir/(?P<caixaId>\d+)/$', 'contas.views.excluirCaixa', name='excluirCaixa'),

    url(r'^sistema/pessoas/$', 'empresas.views.listaPessoas', name='pessoas'),
    url(r'^sistema/pessoas/buscar/$', 'empresas.views.listaPessoas', name='pessoas'),
    url(r'^sistema/pessoas/excluir/(?P<pessoaId>\d+)/$', 'empresas.views.excluirPessoas', name='excluirPessoas'),
    url(r'^sistema/pessoas/editor/$', 'core.views.cadastrarPessoas', name='cadastrarPessoas'),
    url(r'^sistema/pessoas/editor/(?P<pessoaId>\d+)$', 'empresas.views.preencherPessoas', name='cadastrarPessoas'),    
    url(r'^sistema/pessoas/gravar/(?P<pessoaId>\d+)$', 'empresas.views.gravarPessoas', name='gravarPessoas'),
    
    url(r'^sistema/cheque/$', 'contas.views.listarCheque', name='cheque'),
    url(r'^sistema/cheque/editor/$', 'core.views.cadastrarCheque', name='cadastrarCheque'),
    url(r'^sistema/cheque/editor/(?P<chequeId>\d+)$', 'contas.views.preencherCheque', name='preencherCheque'),
    url(r'^sistema/cheque/gravar/$', 'contas.views.gravarCheque', name='gravarCheque'),
    url(r'^sistema/cheque/excluir/(?P<chequeId>\d+)$', 'contas.views.excluirCheque', name='excluirCheque'),

    url(r'^sistema/sistema/$', 'empresas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/sistema/buscar/$', 'empresas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/sistema/editor/$', 'core.views.cadastroSistema', name='cadastroSistema'),
    url(r'^sistema/sistema/editor/(?P<sisId>\d+)/$', 'empresas.views.preencherSistema', name='preencherSistema'),
    url(r'^sistema/sistema/gravar/$', 'empresas.views.gravarSistema', name='gravarSistema'),
    url(r'^sistema/sistema/excluir/(?P<sisId>\d+)/$', 'empresas.views.excluirSistema', name='excluirSistema'),

    url(r'^sistema/usuario/$', 'core.views.usuario', name='usuario'),
    url(r'^sistema/usuario/gravar/$', 'core.views.usuario_gravar', name='usuario_gravar'),

    url(r'^termos-de-uso/$', 'core.views.termos_de_uso', name='termos_de_uso'),
    url(r'^politica-de-privacidade/$', 'core.views.politica_de_privacidade', name='politica_de_privacidade'),
    
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)
