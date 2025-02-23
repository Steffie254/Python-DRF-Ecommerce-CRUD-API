# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6 or later
- Django 3.1 or later
- Django REST Framework

## Installation
After cloning the repository, create a virtual environment:
```
python -m venv env
```
Activate the virtual environment (refer to [this guide](https://docs.python.org/3/tutorial/venv.html) for details).
Install dependencies:
```
pip install -r requirements.txt
```

## API Structure
In our RESTful API, endpoints are structured as follows:

| Endpoint              | HTTP Method | CRUD Method | Description                     |
|----------------------|------------|-------------|---------------------------------|
| `/customers/`        | GET        | READ        | Get all customers              |
| `/customers/:id/`    | GET        | READ        | Get a single customer          |
| `/customers/`        | POST       | CREATE      | Create a new customer          |
| `/customers/:id/`    | PUT        | UPDATE      | Update a customer              |
| `/customers/:id/`    | DELETE     | DELETE      | Delete a customer              |
| `/orders/`           | GET        | READ        | Get all orders                 |
| `/orders/:id/`       | GET        | READ        | Get a single order             |
| `/orders/`           | POST       | CREATE      | Create a new order             |
| `/orders/:id/`       | PUT        | UPDATE      | Update an order                |
| `/orders/:id/`       | DELETE     | DELETE      | Delete an order                |
| `/products/`         | GET        | READ        | Get all products               |
| `/products/:id/`     | GET        | READ        | Get a single product           |
| `/products/`         | POST       | CREATE      | Create a new product           |
| `/products/:id/`     | PUT        | UPDATE      | Update a product               |
| `/products/:id/`     | DELETE     | DELETE      | Delete a product               |
| `/order-items/`      | GET        | READ        | Get all order items            |
| `/order-items/:id/`  | GET        | READ        | Get a single order item        |
| `/order-items/`      | POST       | CREATE      | Create a new order item        |
| `/order-items/:id/`  | PUT        | UPDATE      | Update an order item           |
| `/order-items/:id/`  | DELETE     | DELETE      | Delete an order item           |
| `/payments/`         | GET        | READ        | Get all payments               |
| `/payments/:id/`     | GET        | READ        | Get a single payment           |
| `/payments/`         | POST       | CREATE      | Create a new payment           |
| `/payments/:id/`     | PUT        | UPDATE      | Update a payment               |
| `/payments/:id/`     | DELETE     | DELETE      | Delete a payment               |

## Usage
Use [curl](https://curl.haxx.se/), [httpie](https://github.com/jakubroztocil/httpie#installation), or [Postman](https://www.postman.com/) to test the API.

### Start the Server
```
python manage.py runserver
```

### Authentication
Only authenticated users can access the API:
```
http http://127.0.0.1:8000/api/v1/products/ "Authorization: Bearer {TOKEN}"
```

### User Registration & Token Generation
Create a user:
```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
Get an access token:
```
http POST http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```
Refresh the access token:
```
http POST http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="{REFRESH_TOKEN}"
```

## API Commands
```
Get all products:
http GET http://127.0.0.1:8000/api/v1/products/ "Authorization: Bearer {TOKEN}"

Get a single product:
http GET http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {TOKEN}"

Create a product:
http POST http://127.0.0.1:8000/api/v1/products/ "Authorization: Bearer {TOKEN}" name="Product Name" price=100.00 stock=50

Update a product:
http PUT http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {TOKEN}" name="Updated Name"

Delete a product:
http DELETE http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {TOKEN}"
```

## Pagination & Filtering
- Default page size: `10`
- Adjust page size using `?page_size=` parameter.

Example:
```
http GET http://127.0.0.1:8000/api/v1/products/?page=2 "Authorization: Bearer {TOKEN}"
```
Filter products:
```
http GET http://127.0.0.1:8000/api/v1/products/?name="Product Name" "Authorization: Bearer {TOKEN}"
http GET http://127.0.0.1:8000/api/v1/products/?price=100 "Authorization: Bearer {TOKEN}"
```

