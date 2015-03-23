from django.shortcuts import render
from empresas.forms import LoginForm

def index(request):
    return render(request,'index/index.html')

def login(request):
    form = LoginForm()
    return render(request,'index/login.html', {'form':form})

def valida_login(request):
    return render(request,'index/login.html')

def cadastro(request):
    return render(request,'index/cadastro.html')

def valida_cadastro(request):
    return render(request,'index/cadastro.html')

def sistema(request):
    return render(request,'sistema/index2.html')

def cadastroSistema(request):
    return render(request,'sistema/sistema.html')

def cadastroEmpresa(request):
    return render(request,'sistema/empresa.html')

   



