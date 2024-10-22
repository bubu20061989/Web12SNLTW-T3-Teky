from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Warehouse, Product, Cart, CartItem

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

# Đăng ký Warehouse (Kho hàng)
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_id', 'name', 'location', 'capacity', 'current_stock')
    search_fields = ('name', 'warehouse_id', 'location')
    list_filter = ('location',)
    ordering = ('name',)

# Đăng ký Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'type', 'value', 'amount', 'status', 'warehouse', 'warehouse_stock')
    search_fields = ('product_id', 'type')
    list_filter = ('status', 'type', 'warehouse')
    ordering = ('type', 'warehouse')

# Đăng ký Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'get_username', 'status', 'created_at', 'total_price')  # Tùy chỉnh các trường hiển thị
    search_fields = ('cart_id', 'user_id__username')  
    list_filter = ('status', 'created_at')  
    ordering = ('-created_at',)  

    def get_username(self, obj):
        return obj.user_id.username  # Trả về tên người dùng
    get_username.short_description = 'Username'  # Đặt tiêu đề cho cột

# Đăng ký CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'product_id', 'warehouse', 'quantity', 'price')  # Hiển thị thêm trường warehouse
    search_fields = ('cart_id__cart_id', 'product_id__product_id')  # Cho phép tìm kiếm bằng ID giỏ hàng hoặc sản phẩm
    list_filter = ('cart_id', 'product_id', 'warehouse')  # Lọc theo giỏ hàng, sản phẩm và kho
    ordering = ('cart_id', 'product_id', 'warehouse')
