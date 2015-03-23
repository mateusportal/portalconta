from django.shortcuts import render

def index(request):
    return render(request,'index/index.html')

def login(request):
    return render(request,'index/login.html')

def valida_login(request):
    return render(request,'index/login.html')

def cadastro(request):
    return render(request,'index/cadastro.html')

def valida_cadastro(request):
    return render(request,'index/cadastro.html')

def sistema(request):
    return render(request,'sistema/index2.html')

def calendario(request):
    return render(request,'sistema/calendario.html')    



