from django.shortcuts import render, redirect
from myapp.forms import ImovelForm, LocatarioForm
from .models import Imovel, ImagemImovel


def lista_locacao(request):
    imoveis = Imovel.objects.filter(is_locate=False)
    context = {
    'imoveis': imoveis}
    return render(request, 'lista_locacao.html', context)

def form_locatario(request):
    form = LocatarioForm() 
    if request.method == 'POST':
        form = LocatarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_locacao')   
    return render(request, 'form_locatario.html', {'form': form})


def form_imovel(request):
    form = ImovelForm()
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            ##Se form for válido salva
            imovel = form.save()
            ##Pega todas as imagens
            files = request.FILES.getlist('immobile') 
            if files:
                for f in files:
                    ##Cria instance para imagens
                    ImagemImovel.objects.create( 
                        imovel=imovel, 
                        image=f)
            return redirect('lista_locacao')  
    return render(request, 'form_imovel.html', {'form': form})
