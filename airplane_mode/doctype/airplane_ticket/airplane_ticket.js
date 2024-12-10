frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add custom button to the form
        frm.add_custom_button(__('Set Seat Number'), function() {
            // Open dialog to get seat number
            frappe.prompt({
                label: __('Seat Number'),
                fieldname: 'seat_number',
                fieldtype: 'Data',
                reqd: 1  // Make this field required
            }, function(values) {
                // Set the entered seat number to the Seat field in the form
                frm.set_value('seat', values.seat_number);
            }, __('Enter Seat Number'), __('Submit'));
        });
    }
});