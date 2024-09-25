from django import forms
from .models import Employee,Product

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
    class Meta:
        model = Product
        fields = ['product_id', 'value', 'type', 'amount', 'status']  # Include all fields from the model
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-input'}),
            'value': forms.NumberInput(attrs={'step': '1','class': 'form-input'}),
            'type': forms.TextInput(attrs={'class': 'form-input'}),
            'amount': forms.TextInput(attrs={'class': 'form-input'}),
            'status': forms.Select(choices=Product.STATUS_CHOICES),
        }
