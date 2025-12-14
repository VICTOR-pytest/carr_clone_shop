from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import carr as CarrModel


# LIST - Listar todos os carros
def carr_list(request):
    carrs = CarrModel.objects.all()
    return render(request, 'carr/carr_list.html', {'carrs': carrs})


# READ - Detalhe de um carro
def carr_detalhe(request, id):
    carro = get_object_or_404(CarrModel, id=id)
    return render(request, 'carr/carr_detalhe.html', {'carr': carro})


# CREATE - Criar novo carro
def carr_criar(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        
        if name and model and year and price:
            carro = CarrModel.objects.create(
                name=name,
                model=model,
                year=int(year),
                price=float(price)
            )
            return redirect('carr_detalhe', id=carro.id)
    
    return render(request, 'carr/carr_form.html', {'action': 'Criar'})


# UPDATE - Editar carro existente
def carr_editar(request, id):
    carro = get_object_or_404(CarrModel, id=id)
    
    if request.method == 'POST':
        carro.name = request.POST.get('name', carro.name)
        carro.model = request.POST.get('model', carro.model)
        carro.year = int(request.POST.get('year', carro.year))
        carro.price = float(request.POST.get('price', carro.price))
        carro.save()
        return redirect('carr_detalhe', id=carro.id)
    
    return render(request, 'carr/carr_form.html', {
        'action': 'Editar',
        'carro': carro
    })


# DELETE - Deletar carro
def carr_deletar(request, id):
    carro = get_object_or_404(CarrModel, id=id)
    
    if request.method == 'POST':
        carro.delete()
        return redirect('carr_list')
    
    return render(request, 'carr/carr_confirmar_delete.html', {'carro': carro})


# FILTER - Filtrar por marca
def carr_por_marca(request, marca):
    carros = CarrModel.objects.filter(name=marca)
    return render(request, 'carr/carr_list.html', {'carrs': carros})