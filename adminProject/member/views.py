from django.http import HttpResponse
from django.template import loader
from .forms import EmployeeForm, ProductForm
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee, Product
from django.contrib.auth import authenticate, login
from django.contrib import messages


def loadNhanSu(request):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nhanSu')
    else: 
        form = EmployeeForm()
    # Query the database for all employees
    employees = Employee.objects.all()
    return render(request, 'nhanSu.html', {'form': form, 'employees': employees})


def updateNhanSu(request, employee_id):
    print('Update NhanSu')
    employee = get_object_or_404(Employee, employee_id=employee_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('nhanSu')  # Redirect về trang danh sách nhân viên
    else:
        form = EmployeeForm(instance=employee)    
    return render(request, 'nhanSu.html', {'form': form})


def deleteNhanSu(request, employee_id):
    print('Delete NhanSu')
    employee = get_object_or_404(Employee, employee_id=employee_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        employee.delete()  # Xóa nhân viên
        return redirect('nhanSu')  # Redirect về trang danh sách nhân viên   
    return render(request, 'nhanSu.html', {'employee': employee})


def loadProduct(request):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else: 
        form = ProductForm()
    # Query the database for all employees
    product = Product.objects.all()

    return render(request, 'Product.html', {'form': form, 'Products': product})

def updateProduct(request, product_id):
    print('Update Product')
    product = get_object_or_404(Product, product_id=product_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')  # Redirect về trang danh sách nhân viên
    else:
        form = ProductForm(instance=product)   
    return render(request, 'Products.html', {'form': form})


def deleteProduct(request, product_id):
    print('Delete Product')
    product = get_object_or_404(Product, product_id=product_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        product.delete()  # Xóa nhân viên
        return redirect('product')  # Redirect về trang danh sách nhân viên  
    return render(request, 'product.html', {'Products': product})

def loadShopProduct(request):
    print('Load Shop Product')
    #check product ow trang thai nao
    product = Product.objects.all()
    print(product)
    return render(request, 'Shop.html', {'Products': product})

def loadLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product')  # Redirect to the 'nhanSu' page after login

        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')
    return render(request, 'login.html')

def loadError(request):
    return render(request, 'error.html')

def loadDangKi(request):
    return render(request, 'dangKi.html')

def loadLogout(request):
    return render(request, 'logout.html')