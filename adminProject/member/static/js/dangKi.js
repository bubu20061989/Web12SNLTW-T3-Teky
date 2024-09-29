document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Lấy giá trị của các trường
    var name = document.getElementById('name').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message');

    // Kiểm tra các trường có rỗng không
    if (!name || !phone || !email) {
        message.textContent = "Vui lòng điền đầy đủ thông tin.";
        return;
    }

    // Kiểm tra định dạng email
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        message.textContent = "Email không hợp lệ.";
        return;
    }

    // Kiểm tra định dạng số điện thoại (chỉ chứa số và dài 10-11 ký tự)
    var phonePattern = /^[0-9]{10,11}$/;
    if (!phonePattern.test(phone)) {
        message.textContent = "Số điện thoại không hợp lệ.";
        return;
    }

    // Nếu tất cả đều đúng
    message.textContent = "Đăng ký thành công!";
    message.style.color = "green";
});
