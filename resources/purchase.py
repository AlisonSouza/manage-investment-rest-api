from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel
from datetime import datetime

class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('purchase_date', required=True)

    parser.add_argument('quantity',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            data = Purchase.parser.parse_args()
            purchase_date = datetime.strptime(data['purchase_date'], "%Y-%m-%d")
            purchase = PurchaseModel(data['price'], data['quantity'], company.id, purchase_date)
            try:
                purchase.save()
            except:
                return {"message": "An error occurred inserting the purchase."}, 500
        else:
            return {"message": "Company not found."}, 204
        return purchase.json(), 201

class PurchaseList(Resource):
    def get(self):
        return {"purchases": [x.json() for x in PurchaseModel.query.all()]}, 200