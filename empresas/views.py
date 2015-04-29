# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from empresas.models import Sistema,Pessoa
from django.contrib.auth.decorators import login_required # USAR: @login_required
from empresas.forms import PessoaForm
from django.utils.translation import ugettext as _


def listaSistema(request):
    if request.method == 'POST':
        sistemas = Sistema.objects.filter(Q(nome__contains=request.POST.get('parametro','')) | Q(tipo__contains=request.POST.get('parametro',''))).order_by('tipo','nome')    

        print request.POST.get('parametro','')

    else:
        sistemas = Sistema.objects.filter(empresa_id=request.user.empresa.id).order_by('tipo','nome')

    return render(request,'sistema/sistema.html',{'sistemas':sistemas})

def gravarSistema(request):
    if request.method == 'POST':
        try:
            sistema = Sistema.objects.get(id=request.POST.get('sisID'),empresa_id=request.user.empresa.id)

        except:
            sistema = Sistema()

        sistema.tipo = request.POST.get('tipo', '').upper()
        sistema.nome = request.POST.get('nome', '').upper()
        sistema.descricao = request.POST.get('descricao','').upper()
        sistema.empresa_id = request.user.empresa.id

        sistema.save()
    
        return HttpResponseRedirect('/sistema/sistema/')

def excluirSistema(request,sisId):
    Sistema.objects.get(id=sisId).delete()
    return HttpResponseRedirect('/sistema/sistema/')

def preencherSistema(request,sisId):
    sistemas = Sistema.objects.get(id=sisId)

    return render(request,'sistema/cadastroSistema.html',{'sistemas':sistemas})

@login_required
def pessoas(request):
    if request.method == 'POST':
        pessoas = Pessoa.objects.filter(empresa_id=request.user.empresa.id, nome__contains=request.POST.get('parametro','')).order_by('nome')
    else:
        pessoas = Pessoa.objects.filter(empresa_id=request.user.empresa.id).order_by('-data_cadastro')[0:12]

    #IMPLEMENTAR PAGINAÇÃO, LISTAR DE 12 EM 12... (COM ORDENAÇÃO)
    return render(request,'sistema/pessoas.html',{'pessoas':pessoas})

@login_required
def pessoas_excluir(request,pessoaId):
    Pessoa.objects.get(id=pessoaId).delete()
    return HttpResponseRedirect('/sistema/pessoas/')

@login_required
def pessoas_formulario(request,pessoaId):
    try:
        if pessoaId:
            pessoa = Pessoa.objects.get(ativo='SIM', pk=pessoaId, empresa_id=request.user.empresa.id)
            form = PessoaForm(instance=pessoa)
        else:
            form = PessoaForm()
    except:
        form = PessoaForm()

    tipos = Sistema.objects.filter(ativo='SIM', tipo='TIPO PESSOA', empresa_id=request.user.empresa.id).order_by('nome')

    return render(request,'sistema/pessoas_formulario.html',{'form':form, 'tipos':tipos})

@login_required
def pessoas_gravar(request):
    if request.method == 'POST':
        tipos = Sistema.objects.filter(ativo='SIM', tipo='TIPO PESSOA', empresa_id=request.user.empresa.id).order_by('nome')

        try:
            pessoa = Pessoa.objects.get(pk=request.POST.get('id','0'), ativo='SIM', empresa_id=request.user.empresa.id)
        except:
            pessoa = Pessoa()

        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save(commit=False)  
            pessoa.save()

            return render(request,'sistema/pessoas.html',{'msg':_(u'Pessoa salva com sucesso!')})
        else:
            return render(request,'sistema/pessoas_formulario.html',{'form':form, 'tipos':tipos})
    else:
        return HttpResponseRedirect('/sistema/pessoas/')





'''
    if request.method == 'POST':
        try:
            pessoa = Pessoa.objects.get(id=request.POST.get('pessoaId'),empresa_id=request.user.empresa.id,
                usuario_id=request.user.id)
        except:
            pessoa = Pessoa()

        pessoa.tipo_id = request.POST.get('tipo','0')
        pessoa.nome = request.POST.get('nome')
        pessoa.cpf = request.POST.get('cpf')
        pessoa.rg = request.POST.get('rg')
        pessoa.conta_banco = request.POST.get('conta_banco')
        pessoa.conta_agencia = request.POST.get('conta_agencia')
        pessoa.conta_corrente = request.POST.get('conta_corrente')
        pessoa.endereco_rua = request.POST.get('endereco_rua').title()
        pessoa.endereco_numero = request.POST.get('endereco_numero')
        pessoa.endereco_complemento = request.POST.get('endereco_complemento')
        pessoa.endereco_bairro = request.POST.get('endereco_bairro')
        pessoa.endereco_cidade = request.POST.get('endereco_cidade')
        pessoa.endereco_estado = request.POST.get('endereco_estado')
        pessoa.endereco_pais = request.POST.get('endereco_pais')
        pessoa.endereco_cep = request.POST.get('endereco_cep')
        pessoa.telefone_fixo = request.POST.get('telefone_fixo')
        pessoa.telefone_celular = request.POST.get('telefone_celular')
        pessoa.email_pessoal = request.POST.get('email_pessoal')
        pessoa.email_empresarial = request.POST.get('email_empresarial')
        pessoa.facebook = request.POST.get('facebook')
        pessoa.twitter = request.POST.get('twitter')
        pessoa.skype = request.POST.get('skype')
        pessoa.googleplus = request.POST.get('googleplus')
        pessoa.empresa_id = request.user.empresa.id
        pessoa.usuario_id = request.user.id

        pessoa.save()
    
        return HttpResponseRedirect('/sistema/pessoas/')
    return HttpResponseRedirect('/')
    '''



