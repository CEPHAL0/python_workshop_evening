class User:
    def __init__(self, username, email, phone, address):
        self.username = username
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        information = f"""
            Username: {self.username}
            Email: {self.email}
            Phone: {self.phone}
            Address: {self.address}
        """
        return information

# Single Inheritance
class Customer(User):
    def __init__(self, username, email, phone, address, customer_id, cart_items, purchase_history):
        super().__init__(username, email, phone, address)
        self.customer_id = customer_id
        self.cart_items = cart_items
        self.purchase_history = purchase_history
    
    def __repr__(self):
        base_information = super().__repr__()

        information = f"""
            Customer ID: {self.customer_id}
            Cart Items: {self.cart_items}
            Purchase History: {self.purchase_history}
        """
        information = base_information + information
        
        return information

class Seller(User):
    def __init__(self, username, email, phone, address, seller_id, store_name, inventory, ratings):
        super().__init__(username, email, phone, address)
        self.seller_id = seller_id
        self.store_name = store_name
        self.inventory = inventory
        self.ratings = ratings


class DeliveryPartner(User):
    def __init__(self, username, email, phone, address, partner_id, vehicle_type, delivery_zone):
        super().__init__(username, email, phone, address)
        self.partner_id = partner_id
        self.vehicle_type = vehicle_type
        self.delivery_zone = delivery_zone

# Creating an object of Seller
seller1 = Seller("alice", "alice@gmail.com", "1111111", "Minnesota", "1451", "Walmart", "Pantry", 4.5)
# print(seller1.address)
# print(seller1.inventory)

# Create an object of customer
customer1 = Customer("john", "john@yahoo.com", "2222222222", "Oklahoma", "4511", "Bread, Butter", "None")
print(customer1)

# Multiple Inheritance
class SellerCustomer(Seller, Customer):
    def __init__(self, username, email, phone, address, customer_id, cart_items, purchase_history, seller_id, store_name, inventory, ratings):
        Seller.__init__(self, username, email, phone, address, seller_id, store_name, inventory, ratings)
        Customer.__init__(self, username, email, phone, address, customer_id, cart_items, purchase_history)

seller_customer_1 = SellerCustomer("alice", "alice@gmail.com", "1111111111", "Minnesota", "4512", "Chips, Deodrant", "15 Times", "1341", "Walmart", "Pantry", 4.5)