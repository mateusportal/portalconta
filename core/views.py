# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from datetime import date, datetime
from empresas.forms import LoginForm, UsuarioForm
from empresas.models import Usuario, Empresa, Sistema
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required # USAR: @login_required
from django.utils.translation import ugettext as _

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sistema/')
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
        return HttpResponseRedirect('/sistema/')
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
                    return HttpResponseRedirect('/sistema/')
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
            empresa.email_contato = form['email'].lower().strip()
            empresa.email_financeiro = form['email'].lower().strip()
            empresa.save()
            
            nomeCompleto = form['first_name'].title().split(' ')
            usuario.first_name = nomeCompleto[0]

            nomeCompletoContador = len(nomeCompleto)

            usuario.last_name = ''
            for x in range(1, nomeCompletoContador):
                usuario.last_name = usuario.last_name+' '+nomeCompleto[x]     

            usuario.last_name = usuario.last_name.strip()
            usuario.email = form['email'].lower().strip()
            usuario.username = form['username'].lower().strip()
            usuario.set_password(form['password'].strip())
            usuario.is_staff = False
            usuario.is_active = True
            usuario.is_superuser = False
            usuario.foto = 'padrao.jpg'
            usuario.idioma = 'pt-br'
            usuario.last_login = datetime.now()
            usuario.date_joined = datetime.now()
            usuario.empresa = empresa
    
            usuario.save()

            sistema = Sistema()
            sistema.tipo = _(u'TIPO PESSOA')
            sistema.nome = _(u'CLIENTE')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'TIPO PESSOA')
            sistema.nome = _(u'FORNECEDOR')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'TIPO PESSOA')
            sistema.nome = _(u'FUNCIONÁRIO(A)')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'CATEGORIA')
            sistema.nome = _(u'CAIXA INTERNO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'CATEGORIA')
            sistema.nome = _(u'CAIXA EXTERNO BANCO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'GRUPO')
            sistema.nome = _(u'PRODUTOS E SERVIÇOS')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'GRUPO')
            sistema.nome = _(u'ADMINISTRATIVO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'GRUPO')
            sistema.nome = _(u'FINANCEIRO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'MANUTENÇÃO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'OUTROS')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'HONORÁRIOS')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'ADIANTAMENTO')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'OUTROS')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'TELEFONIA')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()
            sistema = Sistema()
            sistema.tipo = _(u'SUB-GRUPO')
            sistema.nome = _(u'TAXAS')
            sistema.id_empresa = empresa.pk
            sistema.tags = 'PADRÃO '
            sistema.descricao = _(u'Você pode mudar o nome deste tipo, mas não excluir do sistema.')
            sistema.save()

            return render(request,'index/login.html',{'msg':_(u'Usuário criado com sucesso! Faça o login abaixo.')})
        else:
            return render(request,'index/cadastro.html',{'form':form})
    
    return render(request,'index/cadastro_valida.html')

@login_required
def sistema(request):
    return render(request,'sistema/index2.html')

@login_required
def calendario(request):
    return render(request,'sistema/calendario.html') 

@login_required
def cadastrarPessoas(request):
    tipos = Sistema.objects.filter(ativo='SIM', tipo='TIPO PESSOA').order_by('tipo')

    return render(request,'sistema/cadastroPessoas.html',{'tipos':tipos}) 

@login_required
def pessoas(request):
    return render(request,'sistema/cadastroPessoas.html')       

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
            form = form.cleaned_data

            usuario.first_name = form['first_name'].title().strip()
            usuario.last_name = form['last_name'].title().strip()
            usuario.email = form['email'].lower().strip()
            usuario.empresa_id = request.POST['empresa_id']
            usuario.is_active = True

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






