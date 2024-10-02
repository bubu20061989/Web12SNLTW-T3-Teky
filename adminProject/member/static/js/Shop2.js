function addToCart(productId) {
        // Đường dẫn tới API hoặc view xử lý việc tạo giỏ hàng
        const url = `/createCart/${productId}/`;

        // Gửi yêu cầu POST tới server
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}' // Đảm bảo thêm CSRF token nếu bạn sử dụng Django
            },
            body: JSON.stringify({
                product_id: productId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Sản phẩm đã được thêm vào giỏ!');
            } else {
                alert('Có lỗi xảy ra!');
            }
        })
        .catch(error => console.error('Lỗi:', error));
    }