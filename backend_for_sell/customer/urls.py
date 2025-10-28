from django.urls import path
from . import views
urlpatterns=[
    path('',views.customers_list.as_view(),name='customers_list'),
    path('/<int:pk>',views.one_customer.as_view(),name='customer'),
    path('',views.permissions_list.as_view(),name='permissions_list'),
    path('/<int:pk>',views.one_permission.as_view(),name='permission'),
]