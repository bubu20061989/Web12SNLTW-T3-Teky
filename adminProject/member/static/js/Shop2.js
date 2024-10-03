let cart = {};

// Khởi tạo giỏ hàng khi tải trang
window.onload = function () {
    loadCartFromLocalStorage();
    updateCartUI();
};

// Thêm sản phẩm vào giỏ hàng
function addToCart(productId,price ) {
    if (cart[productId]) {
        cart[productId]++;
        cart[productId].price = price;
        console.log(cart[productId].price)
    } else {
        cart[productId] = 1;
        cart[productId].price = price;
        console.log(cart[productId].price )
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Cập nhật giao diện giỏ hàng
function updateCartUI() {
    const cartItems = document.getElementById('cartItems');
    cartItems.innerHTML = ''; // Xóa các sản phẩm hiện tại trong giỏ hàng

    let total = 0;
    for (let productId in cart) {
        let quantity = cart[productId];
        let price = 10000; // Lấy giá sản phẩm
        total += quantity * price;

        // Tạo phần tử cho từng sản phẩm trong giỏ hàng
        let li = document.createElement('li');
        li.innerHTML = `
            <img src="product${productId}.jpg" alt="Product ${productId}">
            <span>Product ${productId}</span>
            <button onclick="updateQuantity(${productId}, 'minus')">-</button>
            <span>${quantity}</span>
            <button onclick="updateQuantity(${productId}, 'plus')">+</button>
            <span>${price * quantity} VND</span>
            <button onclick="removeFromCart(${productId})">X</button>
        `;
        cartItems.appendChild(li);
    }

    // Cập nhật tổng tiền
    document.getElementById('total-price').textContent = total;
    document.getElementById('cart-count').textContent = Object.values(cart).reduce((a, b) => a + b, 0);
}

// Cập nhật số lượng sản phẩm
function updateQuantity(productId, action) {
    if (action === 'plus') {
        cart[productId]++;
    } else if (action === 'minus' && cart[productId] > 1) {
        cart[productId]--;
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Xóa sản phẩm khỏi giỏ hàng
function removeFromCart(productId) {
    delete cart[productId];
    saveCartToLocalStorage();
    updateCartUI();
}

// Hiển thị giỏ hàng
function showCart() {
    document.getElementById('cartModal').style.display = 'block';
}

// Ẩn giỏ hàng
function hideCart() {
    document.getElementById('cartModal').style.display = 'none';
}

// Checkout
function checkout() {
    alert("Tiến hành thanh toán. Tổng tiền: " + document.getElementById('total-price').textContent + " VND");
    hideCart(); // Ẩn giỏ hàng sau khi thanh toán
}


// Lưu giỏ hàng vào localStorage
function saveCartToLocalStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Tải giỏ hàng từ localStorage
function loadCartFromLocalStorage() {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
    }
}
