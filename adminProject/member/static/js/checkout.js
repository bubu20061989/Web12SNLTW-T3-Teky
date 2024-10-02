// Giá sản phẩm (số nguyên)
let pricePerItem = 200000;

function updateTotalPrice(quantity) {
    let totalPrice = pricePerItem * quantity;
    document.getElementById('total-price').innerText = totalPrice.toLocaleString('vi-VN');
}

function increaseQuantity() {
    let quantity = parseInt(document.getElementById('product-quantity').value);
    quantity++;
    document.getElementById('product-quantity').value = quantity;
    updateTotalPrice(quantity);
}

function decreaseQuantity() {
    let quantity = parseInt(document.getElementById('product-quantity').value);
    if (quantity > 1) {
        quantity--;
        document.getElementById('product-quantity').value = quantity;
        updateTotalPrice(quantity);
    }
}

function placeOrder() {
    let productName = document.getElementById('product-name').innerText;
    let quantity = document.getElementById('product-quantity').value;
    let totalPrice = document.getElementById('total-price').innerText;
    alert(`Bạn đã đặt hàng ${quantity} ${productName} với tổng tiền ${totalPrice} VND.`);
}
