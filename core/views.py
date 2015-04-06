# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from datetime import date, datetime
from empresas.forms import LoginForm, UsuarioForm
from empresas.models import Usuario, Empresa, Sistema
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required # USAR: @login_required

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sistema/')
    else:
        return render(request,'index/index.html')

def termos_de_uso(request):
    return render(request,'index/termosdeuso.html')

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
                    return render(request, 'index/login.html', {'form': form, 'msg':'Usuário desativado do sistema! Cadastre-se novamente.'})
            else:
                return render(request, 'index/login.html', {'form': form, 'msg':'Falha ao retornar o objeto do banco.'})  
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

            empresa.razao_social = 'Empresa '+form['first_name'].strip().title()+' Ltda Me'
            empresa.nome_fantasia = 'EMPRESA '+form['first_name'].upper().strip()
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
            usuario.set_password(form['password'])
            usuario.is_staff = False
            usuario.is_active = True
            usuario.is_superuser = False
            usuario.foto = 'padrao.jpg'
            usuario.idioma = 'pt-br'
            usuario.last_login = datetime.now()
            usuario.date_joined = datetime.now()
            usuario.empresa = empresa
    
            usuario.save()

            return render(request,'index/login.html',{'msg':'Usuário criado com sucesso! Faça o login abaixo.'})
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

def pessoas(request):
    
    return render(request,'sistema/cadastroPessoas.html')       

@login_required
def cadastroEmpresa(request):
    return render(request,'sistema/empresa.html')

def listarSistema(request):
    return render(request,'sistema/sistema.html')

def cadastroSistema(request):
    return render(request,'sistema/cadastroSistema.html')

def usuario(request):
    return render(request,'sistema/usuario.html')

def usuarios(request):
    return render(request,'sistema/usuarios.html')






