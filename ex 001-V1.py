class Category:
    def _init_(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

    def display(Categories):
        for category in Categories:
            print(f"Category:{category.name}, Code:{category.code}, no_of_products:{category.no_of_products}")

class Product(Category):
    def _init_(self, name, code, category, price):
        category.no_of_products += 1
        self.name = name
        self.code = code
        self.category = category.name
        self.price = price

    # sort method for high to low price
    @staticmethod
    def sort_products_high_to_low(Products):
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price <= Products[j].price:
                    Products[i], Products[j] = Products[j], Products[i]

    # sort method for low to high price
    @staticmethod
    def sort_products_low_to_high(Products):
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price >= Products[j].price:
                    Products[i], Products[j] = Products[j], Products[i]

    # Search product code
    def searched_products_code(Products, search_code):
        searched_products = next((product for product in Products if product.code == search_code), None)
        return searched_products

    def display_products_code(Products):
        print("\nProducts sort by price(high to low): ")
        Product.sort_products_high_to_low(Products)
        for product in Products:
            print(f"{product.name} [{product.category}]: {product.price:}")

        Product.sort_products_low_to_high(Products)
        print("\nProducts sort by price(low to high): ")
        for product in Products:
            print(f"{product.name} [{product.category}]: {product.price:}")

        search_code = input("\nEnter the code: ")
        find_products = Product.searched_products_code(Products, search_code)

        if find_products:
            print(f"Find:{find_products.name}, Code:{find_products.code}, Category:{find_products.category}, Price:{find_products.price}")
        else:
            print("No products were found in the search code.")


Category1 = Category("Consumer Product", "C01", 0)
Category2 = Category("Industrial Product", "C02", 0)
Category3 = Category("Service Product", "C03", 0)

Categories = [Category1, Category2, Category3]

Product1 = Product("Food", "P01", Category1, 10.0)
Product2 = Product("Perfume", "P02", Category1, 50.0)
Product3 = Product("Clothes", "P03", Category1, 30.0)
Product4 = Product("Vehicles", "P04", Category2, 90.0)
Product5 = Product("Machinery", "P05", Category2, 40.0)
Product6 = Product("Equipment", "P06", Category2, 60.0)
Product7 = Product("Air travel", "P07", Category3, 70.0)
Product8 = Product("Education", "P08", Category3, 80.0)
Product9 = Product("Medical advice", "P09", Category3, 20.0)
Product10 = Product("Consulting", "P10", Category3, 100.0)

Products =[Product1, Product2, Product3, Product4, Product5, Product6, Product7, Product8, Product9, Product10]

Category = Category.display(Categories)
print(Category)
Product.display_products_code(Products)