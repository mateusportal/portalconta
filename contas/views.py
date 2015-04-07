from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from contas.models import Caixa
from empresas.models import Sistema

def preencherCaixa(request,caixaId):
    caixa = Caixa.objects.get(id=1)
    grupo = Sistema.objects.filter(ativo='SIM', tipo='GRUPO').order_by('nome')
    subgrupo = Sistema.objects.filter(ativo='SIM', tipo='SUB-GRUPO').order_by('nome')
    categoria = Sistema.objects.filter(ativo='SIM', tipo='CATEGORIA').order_by('nome')


    return render(request,'sistema/cadastroCaixa.html',{'caixas':caixa,'grupos':grupo,'subgrupos':subgrupo,'categorias':categoria})






        
    

