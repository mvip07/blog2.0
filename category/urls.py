from django.urls import path
from .views import categoryListView, categoryCreateView, categoryDeatilView, categoryUpdateView, categoryDeleteView, categoryListFilterView

urlpatterns = [
    path('', categoryListView.as_view(), name='category'),
    path('create/', categoryCreateView.as_view(), name='category_create_page'),
    path('detail/<int:pk>/', categoryDeatilView.as_view(), name='category_detail_page'),
    path('update/<int:pk>/', categoryUpdateView.as_view(), name='category_update_page'),
    path('delete/<int:pk>/', categoryDeleteView.as_view(), name='category_delete_page'),
    path('detail/<int:pk>/', categoryListFilterView.as_view(), name='category_filter_list_page'),
]