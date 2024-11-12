console.log("Starting")
document.addEventListener('DOMContentLoaded', () => {
    const productTableBody = document.querySelector('table tbody');
    const deleteButton = document.getElementById('delete-button');
    const mainForm = document.getElementById('main-form'); // Lấy tham chiếu đến biểu mẫu

    let selectedRow = null;
    let selectedMainId = null;

    // Function to handle row selection
    function selectRow(row) {
        if (selectedRow) {
            selectedRow.classList.remove('selected');
        }
        selectedRow = row;
        selectedRow.classList.add('selected');
        
        const cells = row.getElementsByTagName('td');
        selectedMainId = cells[0].textContent; // Giả sử ID ở cột đầu tiên
        console.log(selectedMainId);

        // Populate form fields with selected product data
        document.getElementById('id_user_id').value = cells[0].textContent || '';
        document.getElementById('id_total_price').value = cells[4].textContent || '';
        document.getElementById('id_status').value = cells[3].textContent || '';
    }

    // Add click event listener to each row
    if (productTableBody) {
        productTableBody.addEventListener('click', (event) => {
            const row = event.target.closest('tr');
            if (row) {
                selectRow(row);
            }
        });
    }

    // Handle update button click       

    if (searchCartItem) {
        searchCartItem.addEventListener('click', function() {
            if (selectedMainId) {
                mainForm.action = `cartItems/${selectedMainId}/`; // URL để xóa
                mainForm.submit();
            } else {
                alert('Please select a cart to details');
            }
        });
    }
    // Handle delete button click
    if (deleteCartItem) {
        deleteCartItem.addEventListener('click', function() {
            if (selectedMainId) {
                mainForm.action = `cartAdmin/delete/${selectedMainId}/`; // URL để xóa
                mainForm.submit();
            } else {
                alert('Please select a cart to delete.');
            }
        });
    }
});
