from django.shortcuts import render
from django.db.models import Q
from contas.models import Sistema

# Create your views here.

def listaSistema(request):
	sistemas = Sistema.objects.filter(empresa_id=1)
	return render(request,'sistema/sistema.html',{'sistemas':sistemas})
