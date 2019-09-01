from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudante
from .forms import EstudanteForm
from django.contrib.auth.decorators import login_required
'''Importando login required para pedir login
 quem entrar como admin vai poder ver.
 login: admin; email: admin@admin.com ; senha: admin'''

@login_required
def estudanteList(request):
    estudantes = Estudante.objects.all()

    return render(request, 'estudanteList.html', {'estudantes': estudantes})


@login_required
def estudanteCreate(request):
    form = EstudanteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estudanteList')

    return render(request, 'estudanteCreate.html', {'form': form})


@login_required
def estudanteUpdate(request, id):
    estudante = get_object_or_404(Estudante, pk=id)
    form = EstudanteForm(request.POST or None, instance=estudante)

    if form.is_valid():
        form.save()
        return redirect('estudanteList')

    return render(request, 'estudanteCreate.html', {'form': form})


@login_required
def estudanteDelete(request, id):
    estudante = get_object_or_404(Estudante, pk=id)

    if request.method == 'POST':
        estudante.delete()
        return redirect('estudanteList')

    return render(request, 'estudanteDelete.html', {'estudante': estudante})