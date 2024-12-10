# Copyright (c) 2024, NAINA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airline(Document):
	def validate(self):
        # Ensure website URL is valid if provided
		if self.website and not self.website.startswith(('http://', 'https://')):
			frappe.throw("Website URL must start with http:// or https://")
