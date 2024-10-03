// function addToCart(productId) {
//     fetch(`/createCart/${productId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ product_id: productId })
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert(data.message || 'Failed to add product to cart.');
//     });
// }
let cart = {};

function addToCart(productId) {
    if (cart[productId]) {
        cart[productId]++;
    } else {
        cart[productId] = 1;
    }
    updateCartUI();
}

function updateCartUI() {
    const cartItems = document.getElementById('cartItems');
    cartItems.innerHTML = ''; // Clear current cart items

    let total = 0;
    for (let productId in cart) {
        let quantity = cart[productId];
        let price = getPrice(productId); // Fetch price of the product
        total += quantity * price;

        // Create cart item element
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

    // Update total price
    document.getElementById('total-price').textContent = total;
    document.getElementById('cart-count').textContent = Object.values(cart).reduce((a, b) => a + b, 0);
}

function updateQuantity(productId, action) {
    if (action === 'plus') {
        cart[productId]++;
    } else if (action === 'minus' && cart[productId] > 1) {
        cart[productId]--;
    }
    updateCartUI();
}

function removeFromCart(productId) {
    delete cart[productId];
    updateCartUI();
}

function showCart() {
    document.getElementById('cartModal').style.display = 'block';
}

function hideCart() {
    document.getElementById('cartModal').style.display = 'none';
}

function checkout() {
    alert("Proceeding to payment. Total: " + document.getElementById('total-price').textContent + " VND");
    hideCart(); // Hide cart after checkout
}

function getPrice(productId) {
    // Replace with actual logic to fetch product price
    const prices = {
        1: 100000,
        2: 150000
    };
    return prices[productId];
}
