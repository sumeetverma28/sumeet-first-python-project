# "Build system: Login module- Product list, Cart system, Checkout logic"

username = "Sumeet Verma"
password = "Sumeet@123"
if username == "Sumeet Verma" and password ==  "Sumeet@123" :
     
     product_list = ["Bottle", "Bag", "Pen", "Pencil", "Eraser"]

     cart = []
     item_1 = input("Enter item to add to cart: ")
     cart.append(item_1)

     item_2 = input("Enter item to add to cart: ")
     cart.append(item_2)

     item_3 = input("Enter item to add to cart: ")
     cart.append(item_3)

     print("Items in cart:", cart)
     
     checkout = input("Do you want to proceed to checkout? (yes/no): ")
     if checkout.lower() == "yes":
         print("Proceeding to checkout...")
         # Simulate checkout logic here

else:
     print("Invalid username or password. Cannot add items to cart.")

     

      

 





 
