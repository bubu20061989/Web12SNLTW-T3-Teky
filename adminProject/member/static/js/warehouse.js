document.addEventListener('DOMContentLoaded', () => {
    const productTableBody = document.querySelector('table tbody');
    const updateButton = document.getElementById('update-button');
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
        document.getElementById('id_warehouse_id').value = cells[0].textContent || '';
        document.getElementById('id_name').value = cells[1].textContent || '';
        document.getElementById('id_location').value = cells[2].textContent || '';
        document.getElementById('id_capacity').value = cells[3].textContent || '';
        document.getElementById('id_current_stock').value = cells[4].textContent || '';
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
    if (updateButton) {
        console.log('Update button clicked')
        updateButton.addEventListener('click', function() {
            if (selectedMainId) {
                mainForm.action = `/warehouse/update/${selectedMainId}/`; // URL để cập nhật
                mainForm.submit();
            } else {
                alert('Please select a warehouse to update.');
            }
        });
    }

    // Handle delete button click
    if (deleteButton) {
        deleteButton.addEventListener('click', function() {
            if (selectedMainId) {
                mainForm.action = `warehouse/delete/${selectedMainId}/`; // URL để xóa
                mainForm.submit();
            } else {
                alert('Please select a warehouse to delete.');
            }
        });
    }
});
