from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from inventoryapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list_item/', views.list_item, name='list_item'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('delete_bill/<str:pk>/', views.delete_bill, name="delete_bill"),
    path('search_items',views.search_items,name="search_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue/<str:pk>/', views.issue, name="issue"),
    # path('reorder_level/<str:pk>/', views.reorder, name="reorder"),
    path('receive/<str:pk>/', views.receive, name="receive"),
    path('sales/',views.sales,name="sales"),

    path('',include('authapp.urls')),

    #REST FRAMEWORK URLS
    path('api/',include('api.urls')),


]
