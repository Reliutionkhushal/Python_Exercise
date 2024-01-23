class Category:
    def _init_(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = []

    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.generate_display_name()} > {self.name}"
        else:
            return self.name

    @classmethod
    def sort_products_by_category(cls, Categories):
        for i in range(0, len(Categories)):
            for j in range(i+1, len(Categories)):
                if Categories[i].name > Categories[j].name:
                    Categories[i], Categories[j] = Categories[j], Categories[i]

    def sort_products_by_name(self):
        for i in range(0, len(self.products)):
            for j in range(i+1, len(self.products)):
                if self.products[i].name > self.products[j].name:
                    self.products[i], self.products[j] = self.products[j], self.products[i]

    def display_product(self):
        print(f"Category: {self.name}\nCode: {self.code}\nDisplay Name: {self.display_name}")
        self.sort_products_by_name()
        for product in self.products:
            print(f"Product: {product.name} (Code: {product.code}, Price: {product.price})")

class Product:
    def _init_(self, name, code, category, price):
        category.products.append(self)
        self.name = name
        self.code = code
        self.category = category
        self.price = price

Category1 = Category("Vehicle", "C01")
Category2 = Category("Cars", "C02", parent=Category1)
Category3 = Category("Petroleum", "C03", parent=Category2)
Category4 = Category("EV ", "C04", parent=Category3)
Category5 = Category("Bike", "C05", parent=Category4 )

Product1 = Product("Activa", "P01", Category1,  500.00)
Product2 = Product("Bicycle", "P02", Category1,  150.00)
Product3 = Product("Bus",  "P03", Category1,  400.00)

Product4 = Product("Tata","P04", Category2,  1000.00)
Product5 = Product("Creta", "P05", Category2, 2000.00)
Product6 = Product("BMW", "P06", Category2,  3000.00)

Product7 = Product("Rickshaw", "P07",  Category3, 250.00)
Product8 = Product("Toyota", "P08", Category3, 350.00)
Product9 = Product("Taxi", "P09", Category3,  450.00)

Product10 = Product("Tesla", "P10", Category4,  600.00)
Product11 = Product("Smart Bike", "P11", Category4,  700.00)
Product12 = Product("Smart Car", "P12", Category4,  800.00)

Product13 = Product("TVS", "P13", Category5,  100.00)
Product14 = Product("Royal Bike", "P14", Category5,  110.00)
Product15 = Product("Honda", "P15", Category5,   130.00)

Categories = [Category1, Category2, Category3, Category4, Category5]
Category.sort_products_by_category(Categories)
for category in Categories:
    category.display_product()
    print()

Products = [Product1, Product2, Product3, Product4, Product5, Product6, Product7, Product8,
            Product9, Product10, Product11, Product12, Product13, Product14, Product15]