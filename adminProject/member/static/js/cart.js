document.addEventListener('DOMContentLoaded', () => {
    const productTableBody = document.querySelector('table tbody');
    const deleteButton = document.getElementById('btn-delete');
    const detailButton = document.getElementById('btn-detail');
    const mainForm = document.getElementById('main-form');

    let selectedMainId = null;

    // Function to handle row selection
    function selectRow(row) {
        // Deselect previously selected row
        const previouslySelected = document.querySelector('tr.selected');
        if (previouslySelected) {
            previouslySelected.classList.remove('selected');
        }

        // Select the new row
        row.classList.add('selected');
        
        const cells = row.getElementsByTagName('td');
        selectedMainId = cells[0].textContent.trim(); // Get Cart ID from the first column

        // Populate form fields with selected cart data
        document.getElementById('id_cart_id').value = cells[0].textContent.trim() || '';
        document.getElementById('id_total_price').value = cells[4].textContent.trim() || '';
        document.getElementById('id_status').value = cells[3].textContent.trim() || '';

        // Enable buttons
        deleteButton.disabled = false;
        detailButton.disabled = false;
    }

    // Add click event listener to rows
    if (productTableBody) {
        productTableBody.addEventListener('click', (event) => {
            const row = event.target.closest('tr');
            if (row) {
                selectRow(row);
            }
        });
    }

    // Handle "Details" button click
    detailButton.addEventListener('click', () => {
        if (selectedMainId) {
            mainForm.action = `/cartItems/${selectedMainId}/`; // URL to view details
            mainForm.submit();
        } else {
            alert('Please select a cart to view details.');
        }
    });

    // Handle "Delete" button click
    deleteButton.addEventListener('click', () => {
        if (selectedMainId) {
            if (confirm('Are you sure you want to delete this cart?')) {
                mainForm.action = `/cartAdmin/delete/${selectedMainId}/`; // URL to delete
                mainForm.submit();
            }
        } else {
            alert('Please select a cart to delete.');
        }
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const productTableBody = document.querySelector('table tbody');
    const deleteButton = document.getElementById('btn-delete');
    const detailButton = document.getElementById('btn-detail');
    const mainForm = document.getElementById('main-form');

    let selectedMainId = null;

    // Function to handle row selection
    function selectRow(row) {
        // Deselect previously selected row
        const previouslySelected = document.querySelector('tr.selected');
        if (previouslySelected) {
            previouslySelected.classList.remove('selected');
        }

        // Select the new row
        row.classList.add('selected');
        
        const cells = row.getElementsByTagName('td');
        selectedMainId = cells[0].textContent.trim(); // Get Cart ID from the first column

        // Populate form fields with selected cart data
        document.getElementById('id_cart_id').value = cells[0].textContent.trim() || '';
        document.getElementById('id_total_price').value = cells[4].textContent.trim() || '';
        document.getElementById('id_status').value = cells[3].textContent.trim() || '';

        // Enable buttons
        deleteButton.disabled = false;
        detailButton.disabled = false;
    }

    // Add click event listener to rows
    if (productTableBody) {
        productTableBody.addEventListener('click', (event) => {
            const row = event.target.closest('tr');
            if (row) {
                selectRow(row);
            }
        });
    }

    // Handle "Details" button click
    detailButton.addEventListener('click', () => {
        if (selectedMainId) {
            mainForm.action = `/cartItems/${selectedMainId}/`; // URL to view details
            mainForm.submit();
        } else {
            alert('Please select a cart to view details.');
        }
    });

    // Handle "Delete" button click
    deleteButton.addEventListener('click', () => {
        if (selectedMainId) {
            if (confirm('Are you sure you want to delete this cart?')) {
                mainForm.action = `/cartAdmin/delete/${selectedMainId}/`; // URL to delete
                mainForm.submit();
            }
        } else {
            alert('Please select a cart to delete.');
        }
    });
});
