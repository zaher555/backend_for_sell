from . import views
from django.urls import path


urlpatterns=[
    path('products',views.products_list.as_view(),name='products_list'),
    path('products/<int:pk>',views.one_product.as_view(),name='product'),
    path('categories',views.categories_list.as_view(),name='categories_list'),
    path('categories/<int:pk>',views.one_category.as_view(),name='category'),
    path('colors',views.colors_list.as_view(),name='colors_list'),
    path('colors/<int:pk>',views.one_color.as_view(),name='color'),
]