from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from contas.models import Caixa, Cheque
from empresas.models import Sistema
from datetime import datetime
#d = datetime.strptime('2007-07-18 10:03:19', '%Y-%m-%d %H:%M:%S')
#day_string = d.strftime('%Y-%m-%d')
#Trabalhando com datas
def caixa_formulario(request,caixaId):
    try:
        caixa = Caixa.objects.get(id=caixaId)
    except:
        caixa = Caixa()

    grupo = Sistema.objects.filter(ativo='SIM', tipo='GRUPO', empresa_id=request.user.empresa.id).order_by('nome')
    subgrupo = Sistema.objects.filter(ativo='SIM', tipo='SUB-GRUPO', empresa_id=request.user.empresa.id).order_by('nome')
    categoria = Sistema.objects.filter(ativo='SIM', tipo='CATEGORIA', empresa_id=request.user.empresa.id).order_by('nome')

    return render(request,'sistema/caixa_formulario.html',{'caixas':caixa,'grupos':grupo,'subgrupos':subgrupo,'categorias':categoria})

def caixa(request):
    caixa = Caixa.objects.filter(empresa_id=int(request.user.empresa.id)).order_by('data_vencimento')

    return render(request,'sistema/caixa.html',{'caixas':caixa})

def caixa_gravar(request):
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

def caixa_excluir(request,caixaId):
    caixa = Caixa.objects.get(empresa_id=request.user.empresa.id,id=caixaId,usuario_id=request.user.id).delete()

    return HttpResponseRedirect('/sistema/caixa/')

def cheque(request):
    if request.method == 'POST':
        cheque = Cheque.objects.filter(valor=request.POST.get('parametro'),empresa_id=int(request.user.empresa.id)).order_by('data_compensar')
    else:
        cheque = Cheque.objects.filter(empresa_id=int(request.user.empresa.id)).order_by('data_compensar')

    return render(request,'sistema/cheque.html',{'cheques':cheque})

def cheque_formulario(request,chequeId):
    try:
        cheque = Cheque.objects.get(id=chequeId)
    except:
        cheque = Cheque()

    return render(request,'sistema/cheque_formulario.html',{'cheques':cheque})

def cheque_gravar(request):
    try:
        cheque = Cheque.objects.get(id=request.POST.get('chequeId'),empresa_id=request.user.empresa.id)
    except:
        cheque = Cheque()

    data_compensar = datetime.strptime(str(request.POST.get('data_compensar')), '%d/%m/%Y').date()
    data_compensado = datetime.strptime(str(request.POST.get('data_compensado')), '%d/%m/%Y').date()
    data_recebido = datetime.strptime(str(request.POST.get('data_recebido')), '%d/%m/%Y').date()

    cheque.numero_cheque = request.POST.get('numero_cheque')
    cheque.valor = (request.POST.get('valor').replace('.','')).replace(',','.')
    cheque.data_compensar = data_compensar.strftime('%Y-%m-%d')
    cheque.data_recebido = data_recebido.strftime('%Y-%m-%d')
    cheque.data_compensado = data_compensado.strftime('%Y-%m-%d')
    cheque.banco = request.POST.get('banco')
    cheque.agencia = request.POST.get('agencia')
    cheque.nome = request.POST.get('nome')
    cheque.empresa_id = request.user.empresa_id

    cheque.save()

    return HttpResponseRedirect('/sistema/cheque/')


def cheque_excluir(request,chequeId):
    cheque = Cheque.objects.get(id=chequeId,empresa_id=request.user.empresa.id).delete()

    return HttpResponseRedirect('/sistema/cheque/')




        
