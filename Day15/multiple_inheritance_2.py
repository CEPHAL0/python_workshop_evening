# E-Commerce System

# Base Entities:

# User → shared parent
# Properties: username, email, phone, address

# Customer(User)
# Unique: customer_id, cart_items, purchase_history

# Seller(User)
# Unique: seller_id, store_name, inventory, ratings

# DeliveryPartner(User)
# Unique: partner_id, vehicle_type, delivery_zone

# Example multiple inheritance:
# (Seller, Customer) → a user who both sells and buys on the platform.

class User:
    username = ''
    email = ''
    phone = ''
    address = ''

# Single Inheritance
class Customer(User):
    seller_id = ''
    cart_items = ''
    purchase_history = ''

class Seller(User):
    seller_id = ''
    store_name = ''
    inventory = ''
    ratings = ''

class DeliveryPartner(User):
    partner_id = ''
    vehicle_type = ''
    delivery_zone = ''

# Multiple Inheritance
class SellerCustomer(Seller, Customer):
    pass