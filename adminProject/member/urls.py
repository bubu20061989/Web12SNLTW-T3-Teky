from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('nhanSu', views.loadNhanSu, name='nhanSu'),
    path('product', views.loadProduct, name='product'),
    path('', views.loadShopProduct, name='shop'),
    path('login', views.loadLogin, name='login'),
    path('dangKi', views.loadDangKi, name='dangKi'),
    path('logout', views.loadLogout, name='logout'),
    # path('home', views.loadHome, name='home'),
    path('createCart/<str:product_id>/', views.createCart, name='error'),
    path('cart', views.loadCart, name='cart'),
    # path('cart/delete/<str:product_id>/', views.deleteCart, name='delete_cart'),
    # path('cart/update/<str:product_id>/<int:quantity>/', views.updateCart, name='update_cart'),
    # path('cart/checkout/', views.checkoutCart, name='checkout_cart'),
    path('error', views.loadError, name='error'),
    path('employee/update/<str:employee_id>/', views.updateNhanSu, name='update_employee'),
    path('employee/delete/<str:employee_id>/', views.deleteNhanSu, name='delete_employee'),
    path('product/update/<str:product_id>/', views.updateProduct, name='update_Product'),
    path('product/delete/<str:product_id>/', views.deleteProduct, name='delete_Product'),
    #/update-employee/TE7091
]
