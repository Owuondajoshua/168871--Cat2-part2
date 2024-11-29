import requests

# Base URL of the API
BASE_URL = "http://127.0.0.1:8000/api/products/"

def add_product(name, description, price):
    """
    Add a new product to the API.
    
    Args:
        name (str): Product name.
        description (str): Product description.
        price (float): Product price.
    """
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print(f"Product added successfully: {response.json()}")
    else:
        print(f"Failed to add product: {response.status_code}, {response.json()}")

def list_products():
    """
    Retrieve and print the list of all products from the API.
    """
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        if products:
            print("Products:")
            for product in products:
                print(f"  - {product['id']}: {product['name']} (${product['price']})")
        else:
            print("No products found.")
    else:
        print(f"Failed to retrieve products: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Example usage of the script
    print("Adding products...")
    add_product("Laptop", "A high-performance laptop.", 1200.99)
    add_product("Smartphone", "A smartphone with great features.", 799.49)
    
    print("\nListing all products...")
    list_products()
