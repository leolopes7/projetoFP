# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)
""" 
@leolopes7 X
https://www.facebook.com/groups/pythonmania/
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from caixas.models import Conta

def index(request):
    return render(request, 'index.html')

def caixasListar(request):
    caixas = Conta.objects.all()[0:10]

    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})


def caixasAdicionar(request):
    return render(request, 'caixas/formCaixas.html')

def caixasSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            caixas = Conta.objects.get(pk=codigo)
        except:
            caixas = Conta()

        caixas.pessoa_id = request.POST.get('pessoa_id', '').upper()
        caixas.tipo = request.POST.get('tipo', '').upper()
        caixas.descricao = request.POST.get('descricao', '').upper()
        caixas.valor = request.POST.get('valor', '').upper()
        caixas.pagseguro = request.POST.get('pagseguro', '').upper()
        #caixas.data = request.POST.get('data', '00/00/0000').upper()

        caixas.save()
    return HttpResponseRedirect('/caixas/')

def caixasPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                caixas = Conta.objects.all()
            else: 
                caixas = Conta.objects.filter(
                    (Q(tipo__contains=textoBusca) |  
                    Q(descricao__contains=textoBusca) | 
                    Q(valor__contains=textoBusca) | 
                    Q(pagseguro__contains=textoBusca))).order_by('-tipo') 
        except:
            caixas = []

        return render(request, 'caixas/listaCaixas.html', {'caixas': caixas, 'textoBusca': textoBusca})

def caixasEditar(request, pk=0):
    try:
        caixas = Conta.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/caixas/')

    return render(request, 'caixas/formCaixas.html', {'caixas': caixas})

def caixasExcluir(request, pk=0):
    try:
        caixas = Conta.objects.get(pk=pk)
        caixas.delete()
        return HttpResponseRedirect('/caixas/')
    except:
        return HttpResponseRedirect('/caixas/')
