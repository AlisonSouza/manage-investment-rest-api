from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('quantity',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            data = Purchase.parser.parse_args()
            
            #purchase = company.purchases.append(PurchaseModel(name, data['price'], company.id))
            print("alison {}".format(data))
            purchase = PurchaseModel(name, data['price'], data['quantity'], company.id)
            try:
                purchase.save_to_db()
            except:
                return {"message": "An error occurred inserting the purchase."}, 500
        else:
            return {"message": "Company not found."}, 204
        return purchase.json(), 201

class PurchaseList(Resource):
    def get(self):
        return {"purchases": [x.json() for x in PurchaseModel.query.all()]}, 200