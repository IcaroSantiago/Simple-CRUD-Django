# Essa parte é 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutosForm

def index (request):
    return render(request, 'dashboard/index.html')

def produtos(request):
    items = Produtos.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/index.html', context)


def add_produtos(request):
    if request.method == "POST":
        form = ProdutosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProdutosForm()
        return render(request,'dashboard/add_new.html', {'form':form})

def edit_produtos(request, pk):
    item = get_object_or_404(Produtos,pk=pk)

    if request.method == "POST":
        form = ProdutosForm(request.POST,instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProdutosForm(instance=item)
        return render(request, 'dashboard/edit_item.html', {'form': form})

def excluir_produtos(request, pk):
    Produtos.objects.filter(id=pk).delete()

    items = Produtos.objects.all()

    context = {
        'items': items
    }

    return render(request,'dashboard/index.html', context)
