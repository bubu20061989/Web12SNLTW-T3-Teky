from .forms import EmployeeForm, ProductForm, WarehouseForm, CartForm, cartItemsForm
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee, Product , CustomUser, Warehouse, CartItem, Cart
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def loadNhanSu(request):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    print(request.method)
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
    employee = get_object_or_404(Employee, employee_id=employee_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        employee.delete()  # Xóa nhân viên
        return redirect('nhanSu')  # Redirect về trang danh sách nhân viên   
    return render(request, 'nhanSu.html', {'employee': employee})



def loadProduct(request):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
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

def loadWarehouse(request):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse')
    else: 
        form = WarehouseForm()
    # Query the database for all employees
    warehouse = Warehouse.objects.all()

    return render(request, 'Warehouse.html', {'form': form, 'Warehouse': warehouse})

def updateWarehouse(request, warehouse_id):
    print('Update Warehouse')
    warehouse = get_object_or_404(Warehouse, warehouse_id=warehouse_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse')  # Redirect về trang danh sách nhân viên
    else:
        form = WarehouseForm(instance=warehouse)   
    return render(request, 'Warehouses.html', {'form': form})

def deleteWarehouse(request, warehouse_id):
    print('Delete Warehouse')
    warehouse = get_object_or_404(Warehouse, warehouse_id=warehouse_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        warehouse.delete()  # Xóa nhân viên
        return redirect('warehouse')  # Redirect về trang danh sách nhân viên  
    return render(request, 'Warehouse.html', {'Warehouse': warehouse})

def loadShopProduct(request):
    print('Load Shop Product')
    #check product ow trang thai nao
    product = Product.objects.all()
    print(product)
    return render(request, 'Shop.html', {'Products': product})

def loadLogin(request):
    # if request.user.is_authenticated():
    #     return render(request, 'login.html')
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            login(request, user) 
            if user.role == 'admin' or user.role == 'manager':
                return redirect('nhanSu')  # Redirect to the 'nhanSu' page after login
            else:
                return redirect('shop')  # Redirect to the 'nhanSu' page after login
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')
    return render(request, 'login.html')

def loadError(request):
    return render(request, 'error.html')

def loadSuccess(request):
    return render(request, 'success.html')

def loadDangKi(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        # 
        email = request.POST['email']
        # user = User.objects.create_user(username, email, password)
        user = CustomUser(
            username=username,
            email=email,
            password = make_password(password),  # Mã hóa mật khẩu,
            role='customer'
        )
        user.save()
        return redirect('login')  # Redirect to the 'nhanSu' page after login
    return render(request, 'dangKi.html')

def loadLogout(request):
    print(request.method)
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'error.html')
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem, Product, CustomUser  # Adjust imports based on your app structure

@csrf_exempt
def createCart(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            cartData = data.get('cartData', None)

            if cartData is None:
                return JsonResponse({'success': False, 'message': 'No cart data provided'})

            # Always create a new cart
            user_cart = Cart.objects.create(user_id=request.user, status='active', total_price=0)

            total_cart_price = 0
            for item in cartData:
                product_id = item['id']
                quantity = item['quantity']
                price = item['price']

                item_total = float(price) * int(quantity)
                total_cart_price += item_total

                # Fetch the Product instance
                try:
                    product = Product.objects.get(product_id=product_id)
                    warehouse = product.warehouse
                except Product.DoesNotExist:
                    return JsonResponse({'success': False, 'message': f'Product with ID {product_id} does not exist'})

                # Add item to the new cart
                CartItem.objects.create(
                    cart_id=user_cart,
                    product_id=product,
                    quantity=quantity,
                    price=price,
                    warehouse=warehouse,
                )

            # Update the total price
            user_cart.total_price = total_cart_price
            user_cart.save()

            return JsonResponse({'success': True, 'message': 'Cart created successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'})

    return render(request, 'success.html')

# @csrf_exempt
# def createCart(request):
#     if request.method == 'POST':
#         try:
#             # Parse JSON data from the request body
#             data = json.loads(request.body)
#             cartData = data.get('cartData', None)
#             #Luu vao cart

#             #luu vao cartitems
#             print(request.user.username)
#             print(cartData)  # Now this should print the cartData
#             return JsonResponse({'success': True, 'message': 'Cart processed successfully'})
#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
#     return render(request, 'checkout.html')

# def loadCheckout(request):
#     return render(request, 'checkout.html')

@login_required
def checkout(request):
    print('checkout')
    cart = Cart.objects.all()
    print(cart)
    return render(request, 'success.html')
    

# @login_required
# def Cart_history(request):
#     Carts = Cart.objects.filter(user=request.user)
#     return render(request, 'checkout.html', {'carts': Carts})


def loadCart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartAdmin')
    else:
        form = CartForm()
    print(form)
    carts = Cart.objects.all()
    return render(request, 'cart.html', {'form': form, 'carts': carts})


def deleteCart(request, cart_id):
    print('Delete CartItems')
    cart = get_object_or_404(CartItem, cart_id=cart_id) 
    if request.method == 'POST':
        cart.delete()  
        return redirect('cartAdmin')  
    return render(request, 'cartAdmin.html', {'cartAdmin': cart})

def loadCartItems(request, cart_id):
    if request.user.role != 'admin' and request.user.role != 'manager':
        return render(request, 'error.html')
    print(request.method)
    if request.method == 'POST':
        form = cartItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartItems')
    else: 
        form = cartItemsForm()
    # Query the database for all employees
    cart = get_object_or_404(CartItem, cart_id=cart_id) 
    return render(request, 'cartItems.html', {'form': form, 'cartItems': cart})


def updateCartItems(request, cart_id):
    print('Update CartItems')
    cart = get_object_or_404(CartItem, cart_id=cart_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        form = cartItemsForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cartItems')  # Redirect về trang danh sách nhân viên
    else:
        form = cartItemsForm(instance=cart)    
    return render(request, 'cartItems.html', {'form': form})

def deleteCartItems(request, cart_id):
    print('Delete CartItems')
    cart = get_object_or_404(CartItem, cart_id=cart_id)  # Kiểm tra nhân viên có tồn tại không
    if request.method == 'POST':
        cart.delete()  # Xóa nhân viên
        return redirect('warehouse')  # Redirect về trang danh sách nhân viên  
    return render(request, 'cartItems.html', {'cartItems': cart})


# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get or create the cart for the logged-in user
#     cart, created = Cart.objects.get_or_create(user=request.user)
    
#     # Get or create the cart item
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
#     if not created:
#         # If the item already exists, increment the quantity
#         cart_item.quantity += 1
#         cart_item.save()
    
#     return redirect('cart_view')

# @login_required
# def update_cart_item(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id)
    
#     # Update the quantity based on user input
#     new_quantity = request.POST.get('quantity', 1)
#     cart_item.quantity = new_quantity
#     cart_item.save()
    
#     return redirect('cart_view')

# @login_required
# def remove_from_cart(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id)
#     cart_item.delete()
    
#     return redirect('cart_view')

