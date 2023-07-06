from django.urls import path
from product_app import views
from django.contrib import admin

urlpatterns=[
    path('',views.load_home,name='load_home'),
    path('category_page',views.category_page,name='category_page'),
    path('add_categorypage',views.add_categorypage,name='add_categorypage'),
    path('product_page',views.product_page,name='product_page'),
    path('add_product',views.add_product,name='add_product'),
    path('show_details',views.show_details,name='show_details'),
    path('show_table',views.show_table,name='show_table'),
]