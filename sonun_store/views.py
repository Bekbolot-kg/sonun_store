from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


class SonunStoreView(generic.ListView):
    template_name = 'store/sonun_store.html'
    queryset = models.Sonun_Store.objects.all()

    def get_queryset(self):
        return models.Sonun_Store.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = 'store/product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Sonun_Store, id=product_id)


class CreateProductView(generic.CreateView):
    template_name = 'crud/create_product.html'
    form_class = forms.StoreForm
    queryset = models.Sonun_Store.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductView, self).form_valid(form=form)


class DeleteProductview(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Sonun_Store, id=product_id)


class UpdateProductView(generic.UpdateView):
    template_name = 'crud/update_product.html'
    form_class = forms.StoreForm
    success_url = '/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Sonun_Store, id= product_id)

    def form_valid(self, form):
        return super(UpdateProductView, self).form_valid(form=form)



class ReviewProductView(generic.CreateView):
    template_name = 'reviews_product.html'
    form_class = forms.ReviewForm
    queryset = models.Reviews.objects.all()
    success_url = '/'

    def form_valid(self, form_review):
        print(form_review.cleaned_data)
        return super(ReviewProductView, self).form_valid(form=form_review)

# def review_product_view(request):
#     method = request.method
#     if method == 'POST':
#         form_review = forms.ReviewForm(request.POST, request.FILES)
#         if form_review.is_valid():
#             form_review.save()
#             return HttpResponse('Коментария добавлен')
#
#     else:
#         form_review = forms.ReviewForm()
#     return render(request, 'reviews_product.html', {'form_review': form_review})


class Search(generic.ListView):
    template_name = 'store/sonun_store.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return models.Sonun_Store.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context