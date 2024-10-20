# Initial product dictionary
products = {
    'IT products': [
        {'name': 'Laptop', 'price': 800},
        {'name': 'Mouse', 'price': 20},
        {'name': 'Keyboard', 'price': 30}
    ],
    'Electronics': [
        {'name': 'Smartphone', 'price': 500},
        {'name': 'Headphones', 'price': 50},
        {'name': 'Speaker', 'price': 100}
    ]
}

# Validate name function
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

# Validate email function
def validate_email(email):
    return '@' in email

# Display categories function
def display_categories():
    print("Categories:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")

# Display products function
def display_products(products_list):
    print("Products:")
    for idx, product in enumerate(products_list, 1):
        print(f"{idx}. {product['name']} - ${product['price']}")

# Display sorted products function
def display_sorted_products(products_list, sort_order):
    # Ensure that products_list contains dictionaries, not tuples
    if all(isinstance(item, dict) for item in products_list):
        if sort_order == "asc":
            return sorted(products_list, key=lambda x: x['price'])
        elif sort_order == "desc":
            return sorted(products_list, key=lambda x: x['price'], reverse=True)
    else:
        raise TypeError("Products list must contain dictionaries.")

# Add to cart function
def add_to_cart(cart, product, quantity):
    # Check that the product is a dictionary
    if isinstance(product, dict):
        cart.append({'name': product['name'], 'price': product['price'], 'quantity': quantity})
    else:
        raise TypeError("Product must be a dictionary.")

# Display cart function
def display_cart(cart):
    if not cart:
        print("Cart is empty.")
    else:
        print("Cart Contents:")
        for item in cart:
            print(f"{item['name']} - {item['quantity']} x ${item['price']}")

# Generate receipt function
def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("\nProducts purchased:")
    for item in cart:
        print(f"{item['name']} - ${item['price']} x {item['quantity']}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Main function
def main():
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please provide both first and last name containing only alphabets.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please provide a valid email address containing '@'.")
        email = input("Enter your email: ")

    cart = []
    total_cost = 0
    while True:
        display_categories()
        category_choice = int(input("Enter the category number: "))
        if category_choice < 1 or category_choice > len(products):
            print("Invalid choice. Please try again.")
            continue
        
        selected_category = list(products.keys())[category_choice - 1]
        product_list = products[selected_category]
        display_products(product_list)

        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = int(input("Enter your option: "))

            if option == 1:
                product_choice = int(input("Enter the product number: "))
                if product_choice < 1 or product_choice > len(product_list):
                    print("Invalid product number. Please try again.")
                    continue
                
                product = product_list[product_choice - 1]
                quantity = int(input("Enter the quantity: "))
                add_to_cart(cart, product, quantity)
                total_cost += product['price'] * quantity
                print(f"Added {quantity} of {product['name']} to the cart.")
            
            elif option == 2:
                sort_order = input("Enter 'asc' for ascending or 'desc' for descending price sort: ")
                sorted_products = display_sorted_products(product_list, sort_order)
                display_products(sorted_products)
            
            elif option == 3:
                break
            
            elif option == 4:
                if cart:
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

if __name__ == "__main__":
    main()
