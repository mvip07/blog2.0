from typing import Any
from .models import Laptop
from django.shortcuts import render
from category.models import Category
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class laptopListView(ListView):
    model = Laptop
    template_name = 'index.html'
    queryset = Laptop.objects.all()
    context_object_name = 'laptops'


class laptopCreateView(CreateView):
    model = Laptop
    template_name = 'laptop/laptop_create_page.html'
    fields = ['title', 'image', 'author', 'price', 'category', 'count', 'price', 'color', 'led_panel', 'processor', 'video_card', 'memory', 'ram', 'keyboard', 'battery']

class laptopDetailView(DetailView):
    model = Laptop
    template_name = 'laptop/laptop_detail_page.html'

    def get(self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        laptops = []
        laptoppp = Laptop.objects.all()
        laptopp = Laptop.objects.filter(id=pk)

        return render(request, self.template_name, {"laptop": laptopp, "laptops": laptoppp})
    

class laptopUpdateView(UpdateView):
    model = Laptop
    template_name = 'laptop/laptop_update_page.html'
    fields = ['title', 'image', 'author', 'price', 'category', 'count', 'price', 'color', 'led_panel', 'processor', 'video_card', 'memory', 'ram', 'keyboard', 'battery']
    success_url = '/'

class laptopDeleteView(DeleteView):
    model = Laptop
    template_name = 'laptop/laptop_delete_page.html'
    success_url = reverse_lazy('index')