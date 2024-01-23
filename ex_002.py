# Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
# •	"type" must be from "company,contact,billing,shipping".
# •	"Company" must be a Customer object which is the parent object.
# •	Apply Multiple possible validation for phone number and email
# •	Does not allowed number in name,city,state and country

# •	Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# •	"company", "billing", "shipping" are objects of Customer.
# •	"date" must be today or the future. Does not allow past date.
# •	"total_amount" auto calculated based on different products inside order.
# •	"order_lines" is list of objects of "OrderLine"

# •	create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# •	"order" is the object of Order.
# •	"subtotal" is auto calculated based on quantity and price.

# •	Display Order and Customer Information
# •	Sort orders based on "date".
# •	User can filter the current month orders
# •	Search Orders from its number.
# •	List/Display all orders of a specific product.
import re
from datetime import datetime, timedelta

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self. state = state
        self.country = country
        self.company = company
        self.type = type

        # Validation methods
        self.validate_email(email)
        self.validate_phone(phone)
        self.validate_type(type)
        self.validate_without_number(name, ["Name", "City", "State", "Country"])

    valid_type = ["company", "contact", "billing", "shipping"]

    # Validation methods
    def validate_email(self, email):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            print("Invalid email format.")

    def validate_phone(self, phone):
        if not re.match(r'^\d{10}$', phone):
            print("Invalid phone number")

    def validate_without_number(self, value, field_name):
        if any(char.isdigit() for char in value):
            print(f"{field_name} cannot contain numbers")

    def validate_type(self, type):
        if type not in self.valid_type:
            print("Invalid type")

class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal()

    def calculate_subtotal(self):
        return self.quantity * self.price

class Order:
    def __init__(self, number, date, company, billing, shipping, order_lines):
        self.number = number
        self.date = self.validate_date(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines
        self.total_amount = self.calculate_total_amount()

    # Date validation method
    def validate_date(self, date):
        today = datetime.now().date()
        if date < today:
            print("Sorry, date must be today or in the future")
        return date

    # Total amount calculation method
    def calculate_total_amount(self):
        total_amount = 0
        for line in self.order_lines:
            total_amount += line.subtotal
        return total_amount

    # Display order and customer information
    def display_order_and_customer_info(self):
        print(f"\nOrder Number: {self.number}")
        print(f"Order Date: {self.date}")
        print(f"Total Amount: {self.total_amount}")
        print(f"Customer Information:")
        print(f"Name: {self.company.name}")
        print(f"Email: {self.company.email}")
        print(f"Phone: {self.company.phone}")
        print(f"Address: {self.company.street}, {self.company.city}, {self.company.state}, {self.company.country}")

    # Sort Orders
    def sorted_order(orders):
        for i in range(0, len(orders)):
            for j in range(0, len(orders)-1):
                if orders[i].date < orders[j].date:
                    orders[i], orders[j] = orders[j], orders[i]

    # Current Month Orders
    def current_month_order(orders):
        current_orders = [order for order in orders if order.date.month == datetime.now().month]
        return current_orders

    # Search Order by Number
    def searched_order_number(orders, search_order):
        searched_number = next((order for order in orders if order.number == search_order), None)
        return searched_number

    # Search Specified Product
    def specified_product(order_lines, search_product):
        searched_product = next((order_line for order_line in order_lines if order_line.product == search_product), None)
        return searched_product

    # List Orders by Product
    def list_orders_by_product(orders, specific_product):
        product_orders = [order for order in orders if any(line.product == specific_product for line in order.order_lines)]
        return product_orders

company_customer1 = Customer("ABC Company", "abc@company.com", "1234567890", "123 Main St", "Jamnagar", "Gujarat", "India", "Reliance", "company")
billing_customer1 = Customer("John Company", "john@email.com", "9876543210", "456 main St", "Faridabad", "Delhi", "India", "TATA", "contact")
shipping_customer1 = Customer("Boss Company", "B@gmail.com", "4253453489", "25 Vivekanand", "Kachchh", "WB", "Afg", "Adani", "billing")

company_customer2 = Customer("XYZ Company", "xyz@company.com", "9876543210", "456 Main St", "Mumbai", "MH", "India", "Infosys", "company")
billing_customer2 = Customer("Jane Company", "jane@email.com", "1234567890", "789 Oak St", "Bangalore", "KA", "India", "Wipro", "contact")
shipping_customer2 = Customer("Tech Company", "tech@gmail.com", "9876543210", "123 Tech St", "Hyderabad", "TS", "India", "TechCorp", "billing")

product1 = "Bike"
product2 = "Car"
product3 = "Bus"

order_line1 = OrderLine("order1", "Bike", 2, 500)
order_line2 = OrderLine("order2", "Car", 1, 200)
order_line3 = OrderLine("order3", "Bus", 3, 300)

order_lines = [order_line1, order_line2, order_line3]

order1 = Order("OR01", datetime.now().date(), company_customer1, billing_customer1, shipping_customer1, [order_line1])
order2 = Order("OR02", datetime.now().date() + timedelta(days=100), company_customer2, billing_customer2, shipping_customer2, [order_line2])
order3 = Order("OR03", datetime.now().date() - timedelta(days=10), company_customer2, billing_customer1, shipping_customer1, [order_line3])

orders = [order1, order2, order3]

print(f"\nDisplay Order and Customer Info: ")
for order in orders:
    Order.display_order_and_customer_info(order)

print("\nSorted Order: ")
Order.sorted_order(orders)
for order in orders:
    print(f"Order Number: {order.number}, Order Date: {order.date}")

print("\nCurrent Month Orders:")
Order.current_month_order(orders)
for order in orders:
    print(f"Order Number: {order.number}, Order Date: {order.date}")

search_order = input("\nEnter the order: ")
found_order = Order.searched_order_number(orders, search_order)
if found_order:
    # print("Found Order: ")
    print(f"Order Number: {found_order.number}, Order Date: {found_order.date}")
else:
    print(f"No order found with number")

search_product = input("\nEnter the Product Name: ")
Order.list_orders_by_product(orders, search_product)
for order in orders:
    print(f"Order Number: {order.number}, Date: {order.date}")
