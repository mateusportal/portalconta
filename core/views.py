# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from datetime import date, datetime
from empresas.forms import LoginForm, UsuarioForm
from empresas.models import Usuario, Empresa, Sistema
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required # USAR: @login_required
from django.utils.translation import ugettext as _
from configuracao_inicial import *

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sistema/'+str(request.user.empresa_id))
    else:
        return render(request,'index/index.html')

def termos_de_uso(request):
    return render(request,'index/termos_de_uso.html')

def politica_de_privacidade(request):
    return render(request,'index/politica_de_privacidade.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sistema/'+str(request.user.empresa_id))
    else:
        form = LoginForm()
        return render(request,'index/login.html', {'form':form})

def valida_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data['username'].lower(), password=form.data['password']) 
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/sistema/'+str(user.empresa_id))
                else:
                    return render(request, 'index/login.html', {'form': form, 'msg':_(u'Usuário desativado do sistema! Cadastre-se novamente.')})
            else:
                return render(request, 'index/login.html', {'form': form, 'msg':_(u'Falha ao retornar o objeto do banco.')})  
        else:
            return render(request, 'index/login.html', {'form': form})    
    else:
        form = LoginForm()
        return render(request, 'index/login.html', {'form': form}) 

def cadastro(request):
    form = UsuarioForm()
    return render(request,'index/cadastro.html', {'form':form})

def valida_cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            usuario = Usuario()
            empresa = Empresa()

            empresa.razao_social = _(u'Empresa ')+form['first_name'].strip().title()+_(u' Ltda Me')
            empresa.nome_fantasia = _(u'EMPRESA ')+form['first_name'].upper().strip()
   
            empresa.save()
            
            nomeCompleto = form['first_name'].title().split(' ')
            usuario.first_name = nomeCompleto[0]

            nomeCompletoContador = len(nomeCompleto)

            usuario.last_name = ''
            for x in range(1, nomeCompletoContador):
                usuario.last_name = usuario.last_name+' '+nomeCompleto[x]     

            usuario.last_name = usuario.last_name.strip()
            usuario.set_password(form['password'].strip())
            usuario.username = form['username'].strip()
            usuario.is_active = True
            usuario.last_login = datetime.now()
            usuario.date_joined = datetime.now()
            usuario.empresa = empresa
    
            usuario.save()

            configuracao_inicial(empresa.id)

            return render(request,'index/login.html',{'msg':_(u'Usuário criado com sucesso! Faça o login abaixo.')})
        else:
            return render(request,'index/cadastro.html',{'form':form})
    
    return render(request,'index/cadastro_valida.html')

@login_required
def sistema(request,empresaId):
    if int(empresaId) == int(request.user.empresa_id):
        if request.LANGUAGE_CODE == 'pt-br':
            fb_lang = 'pt_BR'
        elif request.LANGUAGE_CODE == 'en':
            fb_lang = 'en_US'
        elif request.LANGUAGE_CODE == 'es':
            fb_lang = 'es_ES'

        return render(request,'sistema/index2.html',{'fb_lang':fb_lang})
    else:
        auth_logout(request)
        form = LoginForm()
        return render(request, 'index/login.html', {'form': form, 'msg':_(u'O link que você acessou não é válido!')})

@login_required
def calendario(request):
    return render(request,'sistema/calendario.html')      

@login_required
def cadastroEmpresa(request):
    return render(request,'sistema/empresa.html')

@login_required
def listarSistema(request):
    return render(request,'sistema/sistema.html')

@login_required
def cadastroSistema(request):
    return render(request,'sistema/cadastroSistema.html')

@login_required
def usuario(request):
    try:
        usuario = Usuario.objects.get(pk=request.user.id, is_active=True)
        form = UsuarioForm(instance=usuario)
        return render(request,'sistema/usuario.html',{'form':form})
    except:
        auth_logout(request)
        form = LoginForm()
        return render(request, 'index/login.html', {'form': form, 'msg':_(u'O usuário logado não foi encontrado. Entre novamente no sistema e tente outra vez.')})

@login_required
def usuario_gravar(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(pk=request.user.id, is_active=True)
        form = UsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            usuario = form.save(commit=False)

            if len(request.POST['passwordNovo'].strip()) > 0:
                usuario.set_password(request.POST['passwordNovo'].strip())
                
            usuario.save()
            auth_logout(request)
            form = LoginForm()
            return render(request, 'index/login.html', {'form': form, 'msg':_(u'Os dados de usuário(a) foram alterados com sucesso. Favor, faça login novamente para atualizar a sua tela com os novos dados.')})
        else:
            return render(request,'sistema/usuario.html',{'form':form})
    else:
        return render(request,'sistema/usuario.html',{'form':form})


@login_required
def caixa(request):
    return render(request,'sistema/caixa.html')

@login_required
def cadastrarCaixa(request):
    grupo = Sistema.objects.filter(ativo='SIM', tipo='GRUPO').order_by('nome')
    subgrupo = Sistema.objects.filter(ativo='SIM', tipo='SUB-GRUPO').order_by('nome')
    categoria = Sistema.objects.filter(ativo='SIM', tipo='CATEGORIA').order_by('nome')

    return render(request,'sistema/cadastroCaixa.html',{'grupos':grupo,'subgrupos':subgrupo,'categorias':categoria})

@login_required
def cadastrarCheque(request):
    return render(request,'sistema/cadastroCheque.html')





