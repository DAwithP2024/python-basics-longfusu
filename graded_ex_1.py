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
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x['price'])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x['price'], reverse=True)

# Add to cart function
def add_to_cart(cart, product, quantity):
    if isinstance(product, dict):
        cart.append({'name': product['name'], 'price': product['price'], 'quantity': quantity})
    else:
        raise TypeError("Product must be a dictionary.")

# Display
