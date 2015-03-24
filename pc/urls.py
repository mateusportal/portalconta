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
    url(r'^calendario/$', 'core.views.calendario', name='calendario'),
    url(r'^pessoas/$', 'core.views.pessoas', name='pessoas'),   


    #url(r'^admin/', include(admin.site.urls));
)
