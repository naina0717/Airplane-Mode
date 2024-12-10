// Copyright (c) 2024, NAINA and contributors
// For license information, please see license.txt

// JavaScript code to add hyperlink to the Airline form view
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button(__('Visit Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
        }
    },
    onload: function(frm) { // Correct event name is 'onload', not 'on_load'
        // If the website field is not empty, add a web link
        if (frm.doc.website) {
            frm.add_web_link(('Visit Official Website'), frm.doc.website); // Correct syntax for add_web_link
        }
    }
});

