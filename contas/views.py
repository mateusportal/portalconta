from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from contas.models import Sistema

# Create your views here.

def listaSistema(request):
    if request.method == 'POST':
        sistemas = Sistema.objects.filter(Q(nome__contains=request.POST.get('parametro','')) | Q(tipo__contains=request.POST.get('parametro',''))).order_by('tipo','nome')    

        print request.POST.get('parametro','')

    else:
        sistemas = Sistema.objects.filter(empresa_id=1,).order_by('tipo','nome')

    return render(request,'sistema/sistema.html',{'sistemas':sistemas})

def gravarSistema(request):
    if request.method == 'POST':
        try:
            sistema = Sistema.objects.get(id= request.POST.get('sisID'))

            sistema.tipo = request.POST.get('tipo', '').upper()
            sistema.nome = request.POST.get('nome', '').upper()
            sistema.descricao = request.POST.get('descricao','').upper()

            sistema.save()
        except:
            sistema = Sistema()
            sistema.tipo = request.POST.get('tipo', '').upper()
            sistema.nome = request.POST.get('nome', '').upper()
            sistema.descricao = request.POST.get('descricao','').upper()
            sistema.empresa_id = 1

            sistema.save()
    
        return HttpResponseRedirect('/sistema/sistema/')

def excluirSistema(request,sisId):
    Sistema.objects.get(id=sisId).delete()
    return HttpResponseRedirect('/sistema/sistema/')

def preencherSistema(request,sisId):
    sistemas = Sistema.objects.get(id=sisId)

    return render(request,'sistema/cadastroSistema.html',{'sistemas':sistemas})





        
    

