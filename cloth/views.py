from django.shortcuts import render, redirect
from django.views import View
from . import models
from .forms import OrderForm

class Tag1ClothesView(View):
    template_name = 'cloth/tag1_clothes.html'

    def get(self, request):
        products = models.ProductCL.objects.filter(tag__name='Повседневный')
        return render(request, self.template_name, {'products': products})

class Tag2ClothesView(View):
    template_name = 'cloth/tag2_clothes.html'

    def get(self, request):
        products = models.ProductCL.objects.filter(tag__name='Официальный')
        return render(request, self.template_name, {'products': products})

class Tag3ClothesView(View):
    template_name = 'cloth/tag3_clothes.html'

    def get(self, request):
        products = models.ProductCL.objects.filter(tag__name='Спортивный')
        return render(request, self.template_name, {'products': products})

class Tag4ClothesView(View):
    template_name = 'cloth/tag4_clothes.html'

    def get(self, request):
        products = models.ProductCL.objects.filter(tag__name='Винтажный')
        return render(request, self.template_name, {'products': products})

class AllClothesView(View):
    template_name = 'cloth/all_clothes.html'

    def get(self, request):
        products = models.ProductCL.objects.all()
        return render(request, self.template_name, {'products': products})

class CreateOrderView(View):
    template_name = 'cloth/create_order.html'
    form_class = OrderForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clothes')
        return render(request, self.template_name, {'form': form})
