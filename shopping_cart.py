 
# Simple Shopping Cart Program
 
products = {
    "1": {"name": "Laptop", "price": 1500000},
    "2": {"name": "Phone", "price": 800000},
    "3": {"name": "Headphones", "price": 50000},
    "4": {"name": "Mouse", "price": 25000}
}
 
cart = []
 
print("===== WELCOME TO OUR SHOP =====")
 
while True:
    print("\nAvailable Products:")
    for key, product in products.items():
        print(f"{key}. {product['name']} - UGX {product['price']:,}")
 
    print("5. Checkout")
    print("6. Exit")
 
    choice = input("\nChoose an option: ")
 
    if choice in products:
        product = products[choice]
        cart.append(product)
        print(f"{product['name']} added to your cart!")
 
    elif choice == "5":
        if not cart:
            print("Your cart is empty.")
        else:
            total = sum(item["price"] for item in cart)
 
            print("\n===== YOUR SHOPPING CART =====")
            for item in cart:
                print(f"{item['name']} - UGX {item['price']:,}")
 
            print(f"\nTotal: UGX {total:,}")
            print("Thank you for shopping with us!")
            break
 
    elif choice == "6":
        print("Thank you for visiting our shop!")
        break
 
    else:
        print("Invalid choice. Please try again.")
 
 