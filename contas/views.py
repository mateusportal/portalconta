from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from contas.models import Caixa, Cheque
from empresas.models import Sistema
from datetime import datetime
#d = datetime.strptime('2007-07-18 10:03:19', '%Y-%m-%d %H:%M:%S')
#day_string = d.strftime('%Y-%m-%d')
#Trabalhando com datas
def preencherCaixa(request,caixaId):
    caixa = Caixa.objects.get(id=caixaId)
    grupo = Sistema.objects.filter(ativo='SIM', tipo='GRUPO', empresa_id=request.user.empresa.id).order_by('nome')
    subgrupo = Sistema.objects.filter(ativo='SIM', tipo='SUB-GRUPO', empresa_id=request.user.empresa.id).order_by('nome')
    categoria = Sistema.objects.filter(ativo='SIM', tipo='CATEGORIA', empresa_id=request.user.empresa.id).order_by('nome')


    return render(request,'sistema/cadastroCaixa.html',{'caixas':caixa,'grupos':grupo,'subgrupos':subgrupo,'categorias':categoria})

def listarCaixa(request):
    caixa = Caixa.objects.filter(empresa_id=int(request.user.empresa.id)).order_by('data_vencimento')

    return render(request,'sistema/caixa.html',{'caixas':caixa})

def gravarCaixa(request):
    try:
        caixa = Caixa.objects.get(empresa_id=request.user.empresa.id,id=request.POST.get('caixaId'),usuario_id=request.user.id)
    except:
        caixa = Caixa()

    data_pagamento = datetime.strptime(str(request.POST.get('data_pagamento')), '%d/%m/%Y').date()
    data_vencimento = datetime.strptime(str(request.POST.get('data_vencimento')), '%d/%m/%Y').date()
    data_boleto = datetime.strptime(str(request.POST.get('data_boleto')), '%d/%m/%Y').date()


    caixa.pessoa_id = int(request.POST.get('pessoa_id'))
    caixa.data_pagamento = data_pagamento.strftime('%Y-%m-%d')
    caixa.data_vencimento = data_vencimento.strftime('%Y-%m-%d')
    caixa.valor_multa = (request.POST.get('valor_multa').replace('.','')).replace(',','.')
    caixa.valor_juros = (request.POST.get('valor_juros').replace('.','')).replace(',','.')
    caixa.valor_desconto = (request.POST.get('valor_desconto').replace('.','')).replace(',','.')
    caixa.valor_bruto = (request.POST.get('valor_bruto').replace('.','')).replace(',','.')
    caixa.descricao = request.POST.get('descricao')
    caixa.usuario_id = request.user.id
    caixa.empresa_id = request.user.empresa.id
    caixa.observacao = request.POST.get('observacao')
    caixa.data_boleto = data_boleto.strftime('%Y-%m-%d')
    caixa.categoria_id = request.POST.get('categoria_id')
    caixa.grupo_id = request.POST.get('grupo_id')
    caixa.subgrupo_id = request.POST.get('subgrupo_id')
    caixa.tipo = request.POST.get('tipo')

    caixa.save()

    return HttpResponseRedirect('/sistema/caixa/')

def excluirCaixa(request,caixaId):
    caixa = Caixa.objects.get(empresa_id=request.user.empresa.id,id=caixaId,usuario_id=request.user.id).delete()

    return HttpResponseRedirect('/sistema/caixa/')

def listarCheque(request):
    cheque = Cheque.objects.filter(empresa_id=int(request.user.empresa.id)).order_by('data_compensar')

    return render(request,'sistema/cheque.html',{'cheques':cheque})