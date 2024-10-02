function addToCart(productId) {
    fetch(`/createCart/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || 'Failed to add product to cart.');
    });
}