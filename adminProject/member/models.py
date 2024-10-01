from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=10, unique=True, null=True, blank=True) 
    # Thêm trường role để phân quyền
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Nhân viên'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return f"{self.username} (Employee ID: {self.employee_id}, Role: {self.role})"

# class Customer(models.Model):
#     customer_id = models.CharField(max_length=10, unique=True)
#     customer_name = models.CharField(max_length=100)
#     customer_phone = models.CharField(max_length=15)
#     customer_email = models.EmailField()
#     customer_role = models.CharField(max_length=10, default='customer')
    
#     def __str__(self):
#         return f"{self.customer_name} (Customer ID: {self.customer_id}, Role: {self.customer_role})"
    

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
        ('in_stock', 'In Stock'),
        ('running_out', 'Running Out'),
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
    
# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Cart for {self.user.username}"

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     class Meta:
#         unique_together = ('cart', 'product')

#     def __str__(self):
#         return f"{self.quantity} of {self.product.product_id} in cart"
    
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
