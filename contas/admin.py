from django.contrib import admin
from contas.models import ContaEntrada,ContaSaida,Vinculo,Categoria,Grupo,SubGrupo

admin.site.register(ContaEntrada)
admin.site.register(ContaSaida)
admin.site.register(Vinculo)
admin.site.register(Categoria)
admin.site.register(Grupo)
admin.site.register(SubGrupo)