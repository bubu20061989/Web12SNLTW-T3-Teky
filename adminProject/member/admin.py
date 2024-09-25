from django.contrib import admin
from .models import Employee,Product

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'position', 'hire_date', 'status')
    search_fields = ('name', 'employee_id', 'department')
    list_filter = ('status', 'department', 'position')
    ordering = ('hire_date',)
    readonly_fields = ('employee_id',)  # Make employee_id read-only if you don't want it to be editable

    # Optional: Add any additional customizations here

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'type', 'value', 'amount', 'status')
    search_fields = ('product_id', 'type')
    list_filter = ('status',)
    ordering = ('type',)