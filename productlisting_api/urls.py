from django.urls import path
from .views import ListCategory, DetailCategory, product_list, product_detail, recent_added, best_offer
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='category-detail'),
    path('product', product_list, name='product'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/recent/', recent_added, name='recent_added'),
    path('product/best/', best_offer, name='best_offer'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
