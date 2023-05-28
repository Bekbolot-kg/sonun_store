from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def sonun_view(request):
    return HttpResponse('Salam')


def sonun_store_view(request):
    sonun_store = models.Sonun_Store.objects.all()
    return render(request, 'store/sonun_store.html', {'sonun_store': sonun_store})

def product_detail_view(request, id):
    product_id = get_object_or_404(models.Sonun_Store, id=id)
    return render(request, 'store/product_detail.html', {'product_id': product_id})

def create_product_view(request):
    method = request.method
    if method == 'POST':
        form = forms.StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Продукт добавлен')

    else:
        form = forms.StoreForm()
    return render(request, 'crud/create_product.html', {'form': form})

def delete_product_view(request, id):
    product_id = get_object_or_404(models.Sonun_Store, id=id)
    product_id.delete()
    return HttpResponse('Продукт удален')

def update_product_view(request, id):
    product_id = get_object_or_404(models.Sonun_Store, id=id)
    if request.method == 'POST':
        form = forms.StoreForm(instance=product_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Продукт обновлен')

    else:
        form = forms.StoreForm(instance=product_id)

    return render(request, 'crud/update_product.html', {'form': form, 'product_id': product_id})

def review_product_view(request):
    method = request.method
    if method == 'POST':
        form_review = forms.ReviewForm(request.POST, request.FILES)
        if form_review.is_valid():
            form_review.save()
            return HttpResponse('Коментария добавлен')

    else:
        form_review = forms.ReviewForm()
    return render(request, 'reviews_product.html', {'form_review': form_review})