from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Sumaries(Resource):
    def get(self):
        '''
        company name
        sum of shares
        avarage price
        total amount
        '''
        companies = CompanyModel.query.all()

        sumaries = []
        for company in companies:
            quantity_shares = 0
            total_amount = 0.0
            avarage_price = 0.0
            for purchase in company.purchases:
                quantity_shares += purchase.quantity
                total_amount += purchase.quantity * purchase.price
            avarage_price = total_amount / quantity_shares
            sumaries.append(SumaryDTO(company.name, quantity_shares, avarage_price, total_amount))
        return {'sumaries': [x.json() for x in sumaries]}

class SumaryDTO():
    '''
    company_name
    quantity_shares
    avarage_price
    total_amount
    '''

    def __init__(self, company_name, quantity_shares, avarage_price, total_amount):
        self.company_name = company_name
        self.quantity_shares = quantity_shares
        self.avarage_price = avarage_price
        self.total_amount = total_amount

    def json(self):
        return {'company_name': self.company_name, 'quantity_shares': self.quantity_shares, 'avarage_price': self.avarage_price, 'total_amount': self.total_amount}
