# Copyright (c) 2024, NAINA and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class AirplaneTicket(Document):
# 	pass


import frappe
import random

from frappe.model.document import Document

class AirplaneTicket(Document):
    
    def validate(self):
        total_amount = 0
        unique_add_ons = set()  
        filtered_add_ons = []   


        for item in self.add_ons:
            if item.item not in unique_add_ons:
                unique_add_ons.add(item.item)  
                filtered_add_ons.append(item)  
                total_amount += item.amount  
            else:
                frappe.msgprint(f"Duplicate add-on '{item.item}' found and removed!", alert=True)

        self.add_ons = filtered_add_ons

        self.total_amount = self.flight_price + total_amount
    
    def before_save(self):
        if self.status != "Boarded":
            frappe.throw(f"Cannot save Airplane Ticket unless the status is 'Boarded'.")

    def before_insert(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice('ABCDE')
        self.seat = f"{random_number}{random_letter}"
        


def validate_ticket_creation(doc, method):
    airplane = frappe.get_doc("Airplane", doc.airplane)
    existing_tickets = frappe.db.count('Airplane Ticket', {'flight': doc.flight})
    if existing_tickets >= airplane.capacity:
        frappe.throw(f"Cannot create ticket. Airplane capacity of {airplane.capacity} is full.")


# import frappe

def before_insert(doc, method):
    airplane = frappe.get_doc('Airplane', doc.airplane)
    current_tickets = frappe.db.count('Airplane Ticket', {'airplane': doc.airplane})

    if current_tickets >= airplane.capacity:
        frappe.throw(f'The airplane has reached its capacity of {airplane.capacity} seats.')


# import frappe

def before_insert(doc, method):
    flight = frappe.get_doc('Airplane Flight', doc.flight)
    airplane = frappe.get_doc('Airplane', flight.airplane)
    current_tickets = frappe.db.count('Airplane Ticket', {'flight': doc.flight})
    if current_tickets >= airplane.capacity:
        frappe.throw(f'The airplane has reached its capacity of {airplane.capacity} seats. Cannot book more tickets.')