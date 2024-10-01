

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    cart.push(product);
    document.getElementById("cart-count").innerText = cart.length;
    alert(`Đã thêm ${product.name} vào giỏ hàng!`);
}

function showCart() {
    const cartModal = document.getElementById("cartModal");
    const cartItems = document.getElementById("cartItems");
    cartItems.innerHTML = "";
    cart.forEach(item => {
        cartItems.innerHTML += `<li>${item.name} - ${item.price} VND</li>`;
    });
    cartModal.style.display = "block";
}

function hideCart() {
    document.getElementById("cartModal").style.display = "none";
}

function searchProduct() {
    const searchTerm = document.getElementById("searchInput").value.toLowerCase();
    const filteredProducts = products.filter(product => product.name.toLowerCase().includes(searchTerm));
    const productContainer = document.getElementById("productContainer");
    productContainer.innerHTML = "";
    filteredProducts.forEach(product => {
        productContainer.innerHTML += `
            <div class="product">
                <img src="${product.img}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>Giá: ${product.price} VND</p>
                <button onclick="addToCart(${product.id})">Thêm vào giỏ</button>
            </div>
        `;
    });
}

function showLogin() {
    document.getElementById("loginModal").style.display = "block";
}

function hideLogin() {
    document.getElementById("loginModal").style.display = "none";
}

// function login() {
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;
//     if (username === "admin" && password === "12345") {
//         alert("Đăng nhập thành công!");
//         hideLogin();
//     } else {
//         alert("Tên đăng nhập hoặc mật khẩu không đúng!");
//     }
// }

// Hiển thị sản phẩm khi trang được tải
displayProducts();
