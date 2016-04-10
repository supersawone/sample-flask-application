from flask_restful import Resource

class Customer(Resource):
    def get(self, customer_id):
        return {"data": "Customer {}".format(customer_id)}, 200, {}
