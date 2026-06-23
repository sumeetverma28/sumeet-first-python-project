# Load product data from JSON file
import json
import urllib.request

with open("testdata.json", "r") as f:
    data = json.load(f)
    print(data)
    
# Modify login to handle incorrect input via exceptions
try:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
except Exception as e:
    print(f"Error: {e}")

# Build Login class with validation method
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self):
        try:
            if not self.username or not self.password:
                raise ValueError("Username and password cannot be empty.")
            return True
        except ValueError as e:
            print(f"Validation Error: {e}")
            return False     
login_instance = Login(input_username, input_password)
is_valid = login_instance.validate()
print("Is login valid?", is_valid)

# Create reusable login module
def login(username: str, password: str) -> bool:
    stored_username = "Sumeet Verma"
    stored_password = "Sumeet@123"
    
    if username == stored_username and password == stored_password:
        return True
    else:
        return False
store = login(input_username, input_password)
print("Login successful?", store)   

# Call GET API and print response

with urllib.request.urlopen("https://api.agify.io?name=michael") as response:
    response_data = response.read().decode("utf-8")
    print("GET API Response:")
    print(json.loads(response_data))

# Use list comprehension/filter to filter products with price < 50

filtered_products = [
    product for product in data
    if isinstance(product, dict)
    and isinstance(product.get("price"), (int, float))
    and product["price"] < 50
]
print("Filtered Products (price < 50):")
for product in filtered_products:
    print(product)
