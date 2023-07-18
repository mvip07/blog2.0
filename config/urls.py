"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import homeView, aboutView, blogView, contactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', homeView.as_view(), name='index'),
    path('about/', aboutView.as_view(), name='about'),
    path('blog/', homeView.as_view(), name='blog'),
    path('contact/', homeView.as_view(), name='contact'),
    path('laptop/', include('laptop.urls')),
    path('category/', include('category.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
