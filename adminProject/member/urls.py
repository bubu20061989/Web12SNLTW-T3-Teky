from django.contrib import admin
from django.urls import path
from member import views
from .views import checkout, Cart_history

urlpatterns = [
    path('nhanSu', views.loadNhanSu, name='nhanSu'),
    path('product', views.loadProduct, name='product'),
    path('', views.loadShopProduct, name='shop'),
    path('login', views.loadLogin, name='login'),
    path('dangKi', views.loadDangKi, name='dangKi'),
    path('logout', views.loadLogout, name='logout'),
    path('createCart', views.createCart, name='cart'),
    path('warehouse', views.loadWarehouse, name='warehouse'),
    path('checkout', checkout, name='checkout'),
    path('Cart-history/', Cart_history, name='cart_history'),
    path('error', views.loadError, name='error'),
    path('employee/update/<str:employee_id>/', views.updateNhanSu, name='update_employee'),
    path('employee/delete/<str:employee_id>/', views.deleteNhanSu, name='delete_employee'),
    path('product/update/<str:product_id>/', views.updateProduct, name='update_Product'),
    path('product/delete/<str:product_id>/', views.deleteProduct, name='delete_Product'),
    path('warehouse/update/<str:warehouse_id>/', views.updateWarehouse, name='update_Warehouse'),
    path('warehouse/delete/<str:warehouse_id>/', views.deleteWarehouse, name='delete_Warehouse'),
    #/update-employee/TE7091
]
