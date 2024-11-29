# Product Management REST API using django
A REST API for managing Product resources, implemented using Django and Django REST Framework.

# Features
* POST /api/products/*: Create a new product.
* GET /api/products/*: Retrieve all products.

# Prerequisites
- Python 3.x
- `pip` package manager

# Setup Instructions

1. * Clone Repository: 
   git clone https://github.com/kimutairyan/166907-Cat2.git
   cd product_api

2. * Install Dependencies:
    pip install -r requirements.txt

3. * Run Migrations:
    python manage.py makemigrations
    python manage.py migrate

4. * Run the Server:
    python manage.py runserver
    The server will start at http://127.0.0.1:8000.