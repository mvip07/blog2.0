from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from laptop.models import Laptop
from category.models import Category

class homeView (View):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        laptops = []
        categories = []
        laptopp = Laptop.objects.all()
        categoryy = Category.objects.all()

        print("hi", laptopp)
          
        for x in laptopp:
            laptops.append(Laptop.get_req(x))
        
        for x in categoryy:
            categories.append(Category.get_req(x))

        # new_products = products.__reversed__()

        print("hi", laptops)
        return render(request, self.template_name, {'laptops': laptops, 'categories': categories})
    

class aboutView (TemplateView):
    template_name = 'about.html'

class blogView (TemplateView):
    template_name = 'blog.html'

class contactView (TemplateView):
    template_name = 'contact.html'