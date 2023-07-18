from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category

# Create your views here.

class categoryListView(ListView):
    model = Category
    template_name = 'index.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'

class categoryListFilterView(ListView):
    model = Category
    template_name = 'laptop/laptop_detail_page.html'

class categoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_create_page.html'
    fields = ['title', 'decsciption']

class categoryDeatilView(DetailView):
    model = Category
    template_name = 'laptop/laptop_detail_page.html'

class categoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_update_page.html'
    fields = ['title', 'decsciption']
    
class categoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_delete_page.html'
    success_url = reverse_lazy('index')