

shoppingcart = {}
def addtocart(product, quantity, price):
    if product in shoppingcart:
        shoppingcart[product]["quantity"] += quantity
    else:
        shoppingcart[product] = {"price":price, "quantity": quantity,}
    print(f"{quantity} {product}(s) added to the cart.")



def main():
    
    product = {"apples": 0.5, "bannana": 0.75, "chocolate": 0.25, "mango": 1, "carrot": 0.65}
    while True:
        print("Welcome to your shopping cart")
        print("1. Add a product")
        print("2. Delete a product")
        print("3. View all products")
        print("4. Quit")
        
        choice = int(input("What is your choice (1-4): "))
        if choice == 1:
            newproduct = input("What is the name of the product you would like to add: ").lower()
            if newproduct in product:
                newquantity = int(input("Enter the quantity: "))
                price = product[newproduct]
                addtocart(newproduct, newquantity, price)
            else:
                print("Product not available")
        elif choice == 2:
            removeproduct = input("What product would you like to remove: ").lower()
            removequantity = int(input("How much would you like to remove"))
            removefromcart(removeproduct, removequantity)
            
        elif choice == 3:
            viewcart()
        elif choice ==4:
            print("Goodbye!")
            break
        else:
            print("Invalid Input")

main()
    