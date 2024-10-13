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


class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'Còn hàng'),
        ('running_out', 'Hết hàng'),
        # ('expired', 'Expired'),
    ]
    
    TYPE_CHOICES = [
        ('aoThun', 'Áo Thun'),
        ('aoSoMi', 'Áo Sơ Mi'),
        ('aoKhoac', 'Áo Khoác'),
        ('aoPolo', 'Áo Polo'),
    ]
    
    product_id = models.CharField(max_length=100, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='aoThun',
    )
    amount = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_stock',
    )

    def __str__(self):
        return f'{self.product_id} - {self.type}'
    
class Cart(models.Model):
    TRANG_THAI = [
        ('chuaThanhToan', 'Chưa thanh toán'),
        ('daThanhToan', 'Đã thanh toán'),
    ]

    cart_id = models.CharField(max_length=20, unique=True, primary_key=True)  # Đặt cart_id làm khóa chính
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=TRANG_THAI, default='chuaThanhToan')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Cart {self.cart_id} for {self.user_id.username}"

    class Meta:
        # Bỏ qua khóa chính mặc định
        db_table = 'cart'


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)  # ForeignKey đến Cart
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('cart_id', 'product_id')

    def __str__(self):
        return f"{self.quantity} of {self.product_id} in Cart"

# class HopDong(models.Model):
#     CONTRACT_STATUS_CHOICES = [
#         ('active', 'Active'),
#         ('terminated', 'Terminated'),
#         ('pending', 'Pending'),
#     ] 

#     CONTRACT_TYPE_CHOICES = [
#         ('full_time', 'Full-Time'),
#         ('part_time', 'Part-Time'),
#         ('temporary', 'Temporary'),
#         ('freelance', 'Freelance'),
#     ]

#     contract_id = models.CharField(max_length=20, unique=True)  # ID hợp đồng (unique)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ID nhân viên, liên kết với Employee
#     start_date = models.DateField()  # Ngày ký hợp đồng
#     end_date = models.DateField()  # Ngày kết thúc hợp đồng
#     terms = models.TextField()  # Điều khoản hợp đồng
#     status = models.CharField(max_length=20, choices=CONTRACT_STATUS_CHOICES, default='pending')  # Tình trạng hợp đồng
#     contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES, default='full_time')  # Loại hợp đồng

#     def __str__(self):
#                 return f"Contract {self.contract_id} ({self.employee.name})"
