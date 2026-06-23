# Print name and Age
print("Sumeet Verma")
print("I am 36 years old")

# Create username & password variables
username = "Sumeet Verma"
password = "Sumeet@123"

# Store product list using Python list
x = ["apple", "banana", "cherry"]

# Build login validation (valid vs inLogin Successful)
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

def validate_login(input_username, input_password):
     if input_username == username and input_password == password:
         print("Login Successful")
         return True
      
     else:
         print("inLogin Successful")
         return False
store=validate_login(input_username, input_password) 
print("Validate Login:", store)

# Practice if-else statement to compare two numbers
a = 30
b = 20
if b > a:
   print("b is greater than a")
elif a == b:
   print("a and b are equal")
else:
   print("a is greater than b")

# Loop through product list and print each item
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "apple":
     print(fruit)
  elif fruit == "banana":
     print(fruit)
  elif fruit == "cherry":
     print(fruit)

# Loop through product list and print each item

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Create login function with parameters; return success/failure

def login(username: str, password: str) -> bool:
    # Example stored credentials (in practice, use a secure database or hash)
    stored_username = "admin"
    stored_password = "12345"
    
    if username == stored_username and password == stored_password:
        return True  # Login success
    else:
        return False  # Login failure

store=login(input_username, input_password)
print("Store=",store)
    
   #  Validate login, Store cart items , Simulate checkout#

username = "Sumeet Verma"
password = "Sumeet@123"
if username == "Sumeet Verma" and password ==  "Sumeet@123" :
     cart = []
     item_1 = input("Enter item to add to cart: ")
     cart.append(item_1)

     item_2 = input("Enter item to add to cart: ")
     cart.append(item_2)

     item_3 = input("Enter item to add to cart: ")
     cart.append(item_3)

     print("Items in cart:", cart)

else:
     print("Invalid username or password. Cannot add items to cart.")


     



    
