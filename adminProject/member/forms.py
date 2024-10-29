from django import forms
from .models import Employee,Product, Warehouse, CartItem, Cart

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_id', 'name', 'dob', 'phone', 'address',
            'email', 'department', 'position', 'hire_date', 
            'salary', 'status', 'notes', 
        ]
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}, format='%Y-%m-%d'),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'department': forms.TextInput(attrs={'class': 'form-input'}),
            'position': forms.TextInput(attrs={'class': 'form-input'}),
            'hire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}, format='%Y-%m-%d'),
            'salary': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-input'}),
            'status': forms.Select(
                choices=[
                    ('Active', 'Active'),
                    ('Inactive', 'Inactive'),
                    ('On Leave', 'On Leave'),
                ],
                attrs={'class': 'form-input'}
            ),
            'notes': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-input'}),
        }

        
    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if not employee_id:
            raise forms.ValidationError('Employee ID is required.')
        return employee_id

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary <= 0:
            raise forms.ValidationError('Salary must be a positive number.')
        return salary
    

class ProductForm(forms.ModelForm):
    # Add a ModelChoiceField for the warehouse, and make sure it's not empty
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        empty_label="Chọn kho",  
        widget=forms.Select(attrs={'class': 'form-input'}) 
    )
    employee_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        empty_label="Chọn nhân viên",
        widget=forms.Select(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Product
        fields = ['product_id', 'value', 'type', 'amount', 'status', 'warehouse', 'employee_id']  # Include warehouse
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-input'}),
            'value': forms.NumberInput(attrs={'step': '1', 'class': 'form-input'}),
            'type': forms.Select(choices=Product.TYPE_CHOICES, attrs={'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={'class': 'form-input'}),
            'status': forms.Select(choices=Product.STATUS_CHOICES, attrs={'class': 'form-input'}),
            # The 'warehouse' field already has a class added in its own definition above
        }


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['warehouse_id', 'name', 'location', 'capacity', 'current_stock']  # Include all fields from the model
        widgets = {
            'warehouse_id': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-input'}),
            'current_stock': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['cart_id', 'user_id','status','total_price']   
        widgets = {
            'cart_id': forms.TextInput(attrs={'class': 'form-input'}),
            'user_id': forms.TextInput(attrs={'class': 'form-input'}),
            'status': forms.Select(choices=Cart.TRANG_THAI, attrs={'class': 'form-input'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class cartItemsForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart_id', 'product_id', 'quantity', 'price', 'warehouse']  # Include all fields from the model
        widgets = {
            'cart_id': forms.TextInput(attrs={'class': 'form-input'}),
            'product_id': forms.TextInput(attrs={'class': 'form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'warehouse': forms.TextInput(attrs={'class': 'form-input'}),
        }


