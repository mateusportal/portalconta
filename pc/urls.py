from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index', name='index'),
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^valida_login/$', 'core.views.valida_login', name='valida_login'),
    url(r'^cadastro/$', 'core.views.cadastro', name='cadastro'),
    url(r'^valida_cadastro/$', 'core.views.valida_cadastro', name='valida_cadastro'),
    url(r'^sistema/$', 'core.views.sistema', name='sistema'),
    url(r'^sistema/pessoas/$', 'core.views.pessoas', name='pessoas'),
    url(r'^sistema/listaPessoas/$', 'core.views.listaPessoas', name='listaPessoas'),
    url(r'^sistema/calendario/$', 'core.views.calendario', name='calendario'),
    url(r'^sistema/sistema/$', 'contas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/empresa/$', 'core.views.cadastroEmpresa', name='cadastroEmpresa'),  
    url(r'^sistema/sistema/buscar/$', 'contas.views.listaSistema', name='listaSistema'),
    url(r'^sistema/sistema/editor/$', 'core.views.cadastroSistema', name='cadastroSistema'),
    url(r'^sistema/sistema/editor/(?P<sisId>\d+)/$', 'contas.views.preencherSistema', name='preencherSistema'),
    url(r'^sistema/sistema/gravar/$', 'contas.views.gravarSistema', name='gravarSistema'),
    url(r'^sistema/sistema/excluir/(?P<sisId>\d+)/$', 'contas.views.excluirSistema', name='excluirSistema'),

    url(r'^admin/', include(admin.site.urls)),
)
