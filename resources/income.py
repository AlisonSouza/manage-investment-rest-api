from flask_restful import Resource, Api, reqparse
from models.income import IncomeModel
from models.company import CompanyModel


class Income(Resource):
    parser = reqparse.RequestParser()
    """
    parser.add_argument("-s", 
        "receive_date", 
        help="The Receive Date - format YYYY-MM-DD", 
        required=True, 
        type=lambda d: datetime.strptime(d, '%YYYY%mm%dd')
    )
    """
    parser.add_argument('value',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('income_type',
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self, company_name):
        company = CompanyModel.find_by_name(company_name)

        if company:
            data = Income.parser.parse_args()
            income = IncomeModel(data['value'], data['income_type'], company.id)
            try:
                income.save()
            except:
                return {"message": "An error occurred inserting the income."}, 500
        else:
            return{"message": "Company not found"}, 204
        return income.json()

    def get(self, company_name):
        return {'incomes': [x.json() for x in IncomeModel.query.all()]}