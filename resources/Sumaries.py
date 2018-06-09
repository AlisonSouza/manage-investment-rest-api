from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Sumaries(Resource):
    def get(self):
        companies = CompanyModel.query.all()
        sumaries = []
        for company in companies:
            quantity_shares = 0
            total_amount = 0.0
            avarage_price = 0.0
            total_income = 0.0
            percentage = 0.0
            actual_price = 0.0
            actual_amount = 0.0
            actual_amount_with_income = 0.0
            actual_percentage_with_income = 0.0

            for purchase in company.purchases:
                quantity_shares += purchase.quantity
                total_amount += purchase.quantity * purchase.price
            for income in company.incomes:
                total_income += income.value
            avarage_price = total_amount / quantity_shares
            sumaries.append(SumaryDTO(company.asset, 
                                      quantity_shares,
                                      avarage_price,
                                      total_amount,
                                      total_income,
                                      percentage,
                                      actual_price,
                                      actual_amount,
                                      actual_amount_with_income,
                                      actual_percentage_with_income
            ))
        return {'sumaries': [x.json() for x in sumaries]}

class SumaryDTO():
    def __init__(self, 
                asset, 
                quantity_shares, 
                avarage_price, 
                total_amount, 
                total_income,
                percentage,
                actual_price,
                actual_amount,
                actual_amount_with_income,
                actual_percentage_with_income
                ):
        self.asset = asset
        self.quantity_shares = quantity_shares
        self.avarage_price = avarage_price
        self.total_amount = total_amount
        self.total_income = total_income
        self.percentage = percentage
        self.actual_price = actual_price
        self.actual_amount = actual_amount
        self.actual_amount_with_income = actual_amount_with_income
        self.actual_percentage_with_income = actual_percentage_with_income

    def json(self):
        return {'asset': self.asset, 
                'quantity_shares': self.quantity_shares, 
                'avarage_price': self.avarage_price, 
                'total_amount': self.total_amount,
                'total_income': self.total_income,
                'percentage': self.percentage,
                'actual_price': self.actual_price,
                'actual_amount': self.actual_amount,
                'actual_amount_with_income': self.actual_amount_with_income,
                'actual_percentage_with_income': self.actual_percentage_with_income
                }
