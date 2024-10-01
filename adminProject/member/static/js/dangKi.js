document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log('q')
    // Lấy giá trị của các trường
    var name = document.getElementById('name').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message');

    // Kiểm tra các trường có rỗng không
    if (!name || !phone || !email) {
        message.textContent = "Vui lòng điền đầy đủ thông tin.";
        message.style.color = "red";
        return;
    }

    // Kiểm tra định dạng email
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        message.textContent = "Email không hợp lệ.";
        message.style.color = "red";
        return;
    }

    // Kiểm tra định dạng số điện thoại (chỉ chứa số và dài 10-11 ký tự)
    var phonePattern = /^[0-9]{10,11}$/;
    if (!phonePattern.test(phone)) {
        message.textContent = "Số điện thoại không hợp lệ.";
        message.style.color = "red";
        return;
    }

    // Tạo object chứa dữ liệu
    var formData = {
        name: name,
        phone: phone,
        email: email
    };

    // Gửi dữ liệu đến server bằng fetch
    fetch('/dangki', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}' // CSRF token nếu bạn dùng Django
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            message.textContent = "Đăng ký thành công!";
            message.style.color = "green";
        } else {
            message.textContent = data.error || "Có lỗi xảy ra, vui lòng thử lại.";
            message.style.color = "red";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        message.textContent = "Có lỗi xảy ra, vui lòng thử lại.";
        message.style.color = "red";
    });
});
