from app.resources.customer import Customer
from app import api

api.add_resource(Customer, '/customer/<int:customer_id>')