# Copyright (c) 2024, NAINA and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


import frappe

class VoterList(Document):
    def validate(self):
        if self.age < 18:
            frappe.throw("Person is not eligible for voting")