#Group Work
print("Welcome to Collective Online Shopping Center! Your most reliable and trusted online shop.")

print("\nWhat would you like to purchase today?")


products = {
    'wrist watch': 50,
    'laptop': 12000,
    'air jordan': 250,
    'labubu doll': 1000,
    '128GB pendrive': 100,
    
    
}



cart = []
cost = []

def view_products():
    print("Products available:")
    for item, price in products.items():
        print(item+ '- Ghc' + str(price))


def add_to_cart():
    purchase = input("Please enter the product name: ")
    if purchase in products:
        quantity = int(input("Enter quantity: "))
        if quantity > 0:

            for i in range(quantity):
                cart.append(purchase)
                cost.append(products[purchase])
            print("Items added to cart succcesfully.")
     
        else:
            print("Invalid Input")
        
        
    else:
        print("item unavailable.")


def update_cart():
    purchase = input("Enter product name to remove or change quantity. ")
    if purchase in cart:
        prompt = int(input("Enter 1 to remove the item and 2 to change the quantity of the item. "))
        if  prompt == 1:
            while purchase in cart:
                index = cart.index(purchase)
                del cart[index]
                del cost[index]
            print("Item removed from cart successfully.")

        elif prompt == 2:
            while purchase in cart:
                index = cart.index(purchase)
                del cart[index]
                del cost[index]

            new_quantity = int(input("Enter new quantity: "))
            if new_quantity > 0:
                for i in range(new_quantity):
                    cart.append(purchase)
                    cost.append(products[purchase])
                
            print('Item quantity updated successfully.')
  
        else:
            print("Invalid input")
            
    else:
        print("item not in cart.")

def calculate_total_cost():
    return sum(cost)
 

def print_invoice():
    print("\nInvoice") 
    print("Cart: ") 
    print(cart)
    print("Cost: ")
    print(cost)
    print("Total: Ghc" + str(calculate_total_cost()))

   
def apply_discount():
    count = cart.count('air jordan')
    already_free = cart.count('air jordan') - cost.count(products['air jordan'])

    if count >= 3 and already_free == 0:
        cart.append('air jordan')
        print("You have won a free air jordan shoe.")
    elif count >= 3 and already_free > 0:
        print("Discount already applied!") 
    else:
        print("You are not eligible to receive a discount.")

    
while True:
    print("\n1.View Products \n2.Add to cart \n3.Update cart \n4.View Invoice \n5.Apply for discount \n6.Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        view_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        update_cart()
    elif choice == "4":
        print_invoice()
    elif choice == '5':
        apply_discount()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")  
