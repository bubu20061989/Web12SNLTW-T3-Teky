document.addEventListener('DOMContentLoaded', () => {
    const productTableBody = document.querySelector('table tbody');
    const updateButton = document.getElementById('update-button');
    const deleteButton = document.getElementById('delete-button');
    const mainForm = document.getElementById('main-form'); // Reference to form

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
        selectedMainId = cells[0].textContent; // Assume ID is in the first column
        console.log('Selected Product ID:', selectedMainId);
    
        // Populate form fields with selected product data, skipping the 'image' field
        document.getElementById('id_product_id').value = cells[0]?.textContent || '';
        document.getElementById('id_value').value = cells[1]?.textContent || '';
        document.getElementById('id_type').value = cells[2]?.textContent || '';
        document.getElementById('id_amount').value = cells[3]?.textContent || '';
        document.getElementById('id_status').value = cells[4]?.textContent || '';
        document.getElementById('id_warehouse').value = cells[5]?.textContent || '';
        document.getElementById('id_employee_id').value = cells[6]?.textContent || ''     
        document.getElementById('id_image').value = cells[7]?.textContent || '';
        
        // Do not attempt to set the value of 'image' as it can only be set to an empty string programmatically
        console.log('Form values populated (excluding image field):');
        // console.log({
        //     product_id: document.getElementById('id_product_id').value,
        //     value: document.getElementById('id_value').value,
        //     type: document.getElementById('id_type').value,
        //     amount: document.getElementById('id_amount').value,
        //     status: document.getElementById('id_status').value,
        //     warehouse: document.getElementById('id_warehouse').value,
        //     employee_id: document.getElementById('id_employee_id').value,
        // });
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
                mainForm.action = `/product/update/${selectedMainId}/`; // URL to update
                mainForm.submit();
            } else {
                alert('Please select a product to update.');
            }
        });
    }

    // Handle delete button click
    if (deleteButton) {
        deleteButton.addEventListener('click', function() {
            if (selectedMainId) {
                mainForm.action = `/product/delete/${selectedMainId}/`; // URL to delete
                mainForm.submit();
            } else {
                alert('Please select a product to delete.');
            }
        });
    }
});
