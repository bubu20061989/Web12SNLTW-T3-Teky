from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=10, unique=True, null=True, blank=True) 
    # Thêm trường role để phân quyền
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Nhân viên'),
        ('customer', 'Khách hàng'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return f"{self.username} (Employee ID: {self.employee_id}, Role: {self.role})"


    

class Employee(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On Leave', 'On Leave'),
    ]

    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class Warehouse(models.Model):
    warehouse_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()  # Sức chứa (số lượng sản phẩm có thể lưu trữ)
    current_stock = models.PositiveIntegerField(default=0)  # Số lượng sản phẩm hiện có trong kho
    
    def __str__(self):
        return f"Warehouse {self.name} ({self.warehouse_id})"


class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'Còn hàng'),
        ('running_out', 'Hết hàng'),
    ]
    
    TYPE_CHOICES = [
        ('aoThun', 'Áo Thun'),
        ('aoSoMi', 'Áo Sơ Mi'),
        ('aoKhoac', 'Áo Khoác'),
        ('aoPolo', 'Áo Polo'),
    ]
    image = models.ImageField(upload_to='images', blank=True, null=True)
    product_id = models.CharField(max_length=100, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2) # số lượng sản phẩm trong kho
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='aoThun',
    )
    amount = models.PositiveIntegerField()  # Tổng số lượng sản phẩm
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_stock',
    )
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)  # Kho lưu trữ sản phẩm
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.product_id} - {self.type}'

    
class Cart(models.Model):
    TRANG_THAI = [
        ('chuaThanhToan', 'Chưa thanh toán'),
        ('daThanhToan', 'Đã thanh toán'),
        ('dangGiaoHang', 'Đang giao hàng'),
        ('daGiaoHang', 'Đã giao hàng'),
    ]

    cart_id = models.AutoField(primary_key=True)  # Sử dụng AutoField để tự động tăng
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Trường này chứa ID người dùng
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=TRANG_THAI, default='chuaThanhToan')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Cart {self.cart_id} for {self.user_id.username}"  # Truy cập username từ user_id


    class Meta:
        # Bỏ qua khóa chính mặc định
        db_table = 'cart'

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)  # Xác định sản phẩm lấy từ kho nào

    class Meta:
        unique_together = ('cart_id', 'product_id', 'warehouse')  # Duy nhất dựa trên giỏ hàng, sản phẩm và kho

    def __str__(self):
        return f"{self.quantity} of {self.product_id} from Warehouse {self.warehouse.name} in Cart"


