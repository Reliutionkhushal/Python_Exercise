class Location:
    def _init_(self, name, code):
        self.name = name
        self.code = code

class Movement:
    def _init_(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in movements if movement.product == product]

    def update_stock(self):
        if stock_at_locations[self.product][self.from_location] < self.quantity:
            print(f"Not Enough stock at {self.from_location.name}")

        stock_at_locations[movement.product][movement.from_location] -= movement.quantity
        stock_at_locations[movement.product][movement.to_location] = stock_at_locations[movement.product].get(movement.to_location, 0) + movement.quantity
def print_product_list_by_location(location, stock_at_locations):
    for location in Locations:
        print(f"Location: {location.name}")
        products_at_location = []

        for product, locationsandstock in stock_at_locations.items():
            if location in locationsandstock:
                products_at_location.append((product, locationsandstock[location]))

        if products_at_location:
            for product, stock in sorted(products_at_location):
                print(f"- Product: {product}, Stock: {stock}")
        else:
            print("  No products at this location.")

Location1 = Location("Rajkot", "L01")
Location2 = Location("Ahmedabad", "L02")
Location3 = Location("Vadodara", "L03")
Location4 = Location("Anand", "L04")
Locations = [Location1, Location2, Location3, Location4]

Product1 = "Bike"
Product2 = "Car"
Product3 = "Bus"
Product4 = "Bicycle"
Product5 = "EV"
Products = [Product1, Product2, Product3, Product4, Product5]

stock_at_locations = {
    "Product1": {Location1: 100},
    "Product2": {Location2: 200},
    "Product3": {Location3: 300},
    "Product4": {Location4: 450},
    "Product5": {Location1: 500}
}

Movement1 = Movement(Location1, Location2, "Product1", 30)
Movement2 = Movement(Location2, Location3, "Product2", 80)
Movement3 = Movement(Location3, Location4, "Product3", 120)
Movement4 = Movement(Location4, Location1, "Product4", 180)
Movement5 = Movement(Location1, Location3, "Product5", 200)
movements = [Movement1, Movement2, Movement3, Movement4, Movement5]


for product in stock_at_locations:
    print(f"\nProduct: {product}")

    product_movements = Movement.movements_by_product(product)

    for movement in product_movements:
        print(f"Movements - From: {movement.from_location.name} To: {movement.to_location.name} Quantity: {movement.quantity}")

    print("Stock at Locations:")
    for movement in product_movements:
        movement.update_stock()

    for location, stock in stock_at_locations[product].items():
        print(f"{location.name}, Stock: {stock}")

print(f"\nProduct list by location: ")
print_product_list_by_location(location, stock_at_locations)