from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import forms, models, parser_film
from django.views import generic

class FilmListView(ListView):
    models = models.TvParser
    template_name = 'parser/film_list.html'

    def get_queryset(self):
        return models.TvParser.objects.all()


class ProductListView(ListView):
    models = models.TvParser
    template_name = 'parser/product_list.html'

    def get_queryset(self):
        return models.PrParser.objects.all()

class ParserFormView(FormView):
    template_name = 'parser/parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1> Данные взяты </h1>')
        else:
            return super(ParserFormView).post(*args, **kwargs)

class Searchs(generic.ListView):
    template_name = 'parser/product_list.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return models.PrParser.objects.filter(name__icontains=self.kwargs.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.kwargs.get('q')
        return context
