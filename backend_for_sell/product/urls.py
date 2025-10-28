from . import views
from django.urls import path


urlpatterns=[
    path('',views.productsList.as_view(),name='productsList'),
    path('/<int:pk>',views.one_product.as_view(),name='product'),
    # path('ratings/<int:product_id>/<int:customer_id>', views.customer_rateView.as_view(), name='product_ratings'),
    path('/categories',views.categories_list.as_view(),name='categories_list'),
    path('/categories/<int:pk>',views.one_category.as_view(),name='category'),
    path('/colors',views.colors_list.as_view(),name='colors_list'),
    path('/colors/<int:pk>',views.one_color.as_view(),name='color'),
]