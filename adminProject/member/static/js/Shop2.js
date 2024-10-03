let cart = {};

// Initialize the cart when the page loads
window.onload = function () {
    loadCartFromLocalStorage();
    updateCartUI();
};

// Add product to cart
function addToCart(productId, price) {
    if (cart[productId]) {
        cart[productId].quantity++; // Increase the quantity
    } else {
        cart[productId] = { quantity: 1, price: price }; // Initialize the product with quantity 1
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Update the cart UI
function updateCartUI() {
    const cartItems = document.getElementById('cartItems');
    cartItems.innerHTML = ''; // Clear the current cart items

    let total = 0;
    console.log(cart)
    for (let productId in cart) {
        const item = cart[productId];
        const quantity = item.quantity;
        const price = item.price;

        total += quantity * price; // Update total price
        
        // Create element for each product in the cart
        let li = document.createElement('li');
        li.innerHTML = `
            <span>${productId}</span>
            <button onclick="updateQuantity('${productId}', 'minus')">-</button>
            <span>${quantity}</span>
            <button onclick="updateQuantity('${productId}', 'plus')">+</button>
            <span>${price * quantity} VND</span>
            <button onclick="removeFromCart('${productId}')">X</button>
        `;
        cartItems.appendChild(li);
    }

    // Update total price and cart item count
    document.getElementById('total-price').textContent = total + " VND";
    document.getElementById('cart-count').textContent = Object.values(cart).reduce((a, b) => a + b.quantity, 0);
}

// Update product quantity
function updateQuantity(productId, action) {
    if (action === 'plus') {
        cart[productId].quantity++;
    } else if (action === 'minus' && cart[productId].quantity > 1) {
        cart[productId].quantity--;
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Remove product from cart
function removeFromCart(productId) {
    delete cart[productId];
    saveCartToLocalStorage();
    updateCartUI();
}

// Show the cart modal
function showCart() {
    document.getElementById('cartModal').style.display = 'block';
}

// Hide the cart modal
function hideCart() {
    document.getElementById('cartModal').style.display = 'none';
}

// Checkout
function checkout() {
    const cartData = Object.keys(cart).map(productId => ({
        id: productId,
        quantity: cart[productId].quantity,
        price: cart[productId].price
    }));
    window.location.href = "createCart"
    
    alert("Proceeding to checkout. Total amount: " + document.getElementById('total-price').textContent);
    hideCart(); // Hide cart after checkout


}

// Save cart to localStorage
function saveCartToLocalStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Load cart from localStorage
function loadCartFromLocalStorage() {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
    }
}

{/* <img src="product${productId}.jpg" alt="Product ${productId}"> */}

// #hello
