from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel

class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self, company_name):
        company = CompanyModel.find_by_name(company_name)
        if company:
            data = Purchase.parser.parse_args()
            purchase = Purchase('test', data['price'], company['id'])
            try:
                purchase.save_to_db()
            except:
                return {"message": "An error occurred inserting the purchase."}, 500
        return purchase.json(), 201
