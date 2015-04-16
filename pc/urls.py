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
    url(r'^sistema/pessoas/gravar/$', 'empresas.views.gravarPessoas', name='gravarPessoas'),
    url(r'^sistema/usuarios/$', 'core.views.usuarios', name='usuarios'),
    url(r'^sistema/calendario/$', 'core.views.calendario', name='calendario'),
    url(r'^sistema/sistema/$', 'empresas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/empresa/$', 'core.views.cadastroEmpresa', name='cadastroEmpresa'),  
    url(r'^sistema/sistema/buscar/$', 'empresas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/sistema/editor/$', 'core.views.cadastroSistema', name='cadastroSistema'),
    url(r'^sistema/sistema/editor/(?P<sisId>\d+)/$', 'empresas.views.preencherSistema', name='preencherSistema'),
    url(r'^sistema/sistema/gravar/$', 'empresas.views.gravarSistema', name='gravarSistema'),
    url(r'^sistema/sistema/excluir/(?P<sisId>\d+)/$', 'empresas.views.excluirSistema', name='excluirSistema'),

    url(r'^sistema/usuario/$', 'core.views.usuario', name='usuario'),

    url(r'^admin/', include(admin.site.urls)),
)
