from django.urls import path
from .views import laptopListView, laptopCreateView, laptopDetailView, laptopUpdateView, laptopDeleteView

urlpatterns = [
    path('', laptopListView.as_view(), name='laptop'),
    path('create/', laptopCreateView.as_view(), name='laptop_create_page'),
    path('detail/<int:pk>/', laptopDetailView.as_view(), name='laptop_detail_page'),
    path('update/<int:pk>/', laptopUpdateView.as_view(), name='laptop_update_page'),
    path('delete/<int:pk>/', laptopDeleteView.as_view(), name='laptop_delete_page'),
]