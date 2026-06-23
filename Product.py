class Product:
    comp_name="ACL DIGITAL"
    def __init__(self, product_id : int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price
        print("Product created with ID:", self.product_id, "Name:", self.name, "Price:", self.price)
    
    def extract_product_info(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.3f}"


p1=Product(1, "Laptop", 999.99)
p2=Product(2, "Smartphone", 499.99)
store=p1.extract_product_info()
print("Store=",store)
print("Id=", Product.product_id)
print(type(Product.comp_name))