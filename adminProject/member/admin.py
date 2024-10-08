from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Product, Cart, CartItem

# Đăng ký CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'employee_id', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'employee_id')
    list_filter = ('is_staff', 'is_active', 'role')
    ordering = ('username',)
    readonly_fields = ('employee_id',)  # employee_id chỉ đọc, không thể chỉnh sửa

    # Tùy chỉnh form hiển thị trong admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('employee_id', 'role')}),  # Thêm role và employee_id vào phần quản lý
    )

# Đăng ký Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'position', 'hire_date', 'status')
    search_fields = ('name', 'employee_id', 'department')
    list_filter = ('status', 'department', 'position')
    ordering = ('hire_date',)
    readonly_fields = ('employee_id',)  # employee_id chỉ đọc, không thể chỉnh sửa

# Đăng ký Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'type', 'value', 'amount', 'status')
    search_fields = ('product_id', 'type')
    list_filter = ('status',)
    ordering = ('type',)
    #thay vien

# Register Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user_id', 'status', 'created_at')  # Customize fields to display
    search_fields = ('cart_id', 'user_id__username')  # Allows searching by cart_id or username
    list_filter = ('status', 'created_at')  # Filters for status and creation date
    ordering = ('-created_at',)  # Orders by the most recent carts

# Register CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'product_id', 'quantity', 'price')  # Customize fields to display
    search_fields = ('cart_id__cart_id', 'product_id__product_id')  # Allows searching by cart or product ID
    list_filter = ('cart_id', 'product_id')  # Filters for cart and product
    ordering = ('cart_id', 'product_id')  # Orders by cart and product

# ################################