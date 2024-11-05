from django.contrib import admin
from django.urls import path
from member import views
from .views import checkout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nhanSu', views.loadNhanSu, name='nhanSu'),
    path('product', views.loadProduct, name='product'),
    path('', views.loadShopProduct, name='shop'),
    path('login', views.loadLogin, name='login'),
    path('dangKi', views.loadDangKi, name='dangKi'),
    path('logout', views.loadLogout, name='logout'),
    path('createCart', views.createCart, name='cart'),
    path('cart', views.createCart, name='cart'),
    path('warehouse', views.loadWarehouse, name='warehouse'),
    path('checkout', checkout, name='checkout'),
    # path('Cart-history/', Cart_history, name='cart_history'),
    path('cartItems/', views.loadCartItems, name='cartItems'),
    path('error', views.loadError, name='error'),
    path('employee/update/<str:employee_id>/', views.updateNhanSu, name='update_employee'),
    path('employee/delete/<str:employee_id>/', views.deleteNhanSu, name='delete_employee'),
    path('product/update/<str:product_id>/', views.updateProduct, name='update_Product'),
    path('product/delete/<str:product_id>/', views.deleteProduct, name='delete_Product'),
    path('warehouse/update/<str:warehouse_id>/', views.updateWarehouse, name='update_Warehouse'),
    path('warehouse/delete/<str:warehouse_id>/', views.deleteWarehouse, name='delete_Warehouse'),
    path('cartAdmin/', views.loadCart, name='cartAdmin'),

    #/update-employee/TE7091
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)