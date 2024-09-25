
from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('nhanSu', views.loadNhanSu, name='nhanSu'),
    path('product', views.loadProduct, name='product'),
    path('employee/update/<str:employee_id>/', views.updateNhanSu, name='update_employee'),
    path('employee/delete/<str:employee_id>/', views.deleteNhanSu, name='delete_employee'),
    path('product/update/<str:product_id>/', views.updateProduct, name='update_Product'),
    path('product/delete/<str:product_id>/', views.deleteProduct, name='delete_Product'),
    #/update-employee/TE7091
]
