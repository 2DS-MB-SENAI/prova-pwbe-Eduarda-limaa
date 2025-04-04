from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import Consultaform



def listagem_medicos(request):
    medicos= Medico.objects.all()
    return render(request, 'listar_medicos.html', {'listas': medicos})

def criar_Consultas(request):
    if request.method== 'POST':
        form= Consultaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_medicos')
        else:
            return render(request, 'erro.html')
    else:
        form= Consultaform()
    return render(request, 'form_consulta.html', {'form': form})

def detalhes_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'detalhes.html', {'Detalhes': consulta})






