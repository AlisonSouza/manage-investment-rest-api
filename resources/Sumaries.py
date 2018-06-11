from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Sumaries(Resource):
    def get(self):
        companies = CompanyModel.query.all()
        sumaries = []
        shares_actual_price = {'EGIE3': 34.74, 
                            'ODPV3': 13.12,
                            'LREN3': 29.25,
                            'MDIA3': 38.85,
                            'MOVI3': 6.13,
                            'GRND3': 8.07,
                            'ARZZ3': 42.16,
                            'BBSE3': 25.46,
                            'FLRY3': 24.04,
                            'CIEL3': 16.42,
                            'SMLS3': 48.79,
                            'PSSA3': 41.66,
                            'WEGE3': 16.50
                        }

        for company in companies:
            quantity_shares = 0
            total_amount = 0.0
            avarage_price = 0.0
            total_income = 0.0
            percentage = 0.0
            actual_price = shares_actual_price[company.asset]
            actual_amount = 0.0
            actual_amount_with_income = 0.0
            actual_percentage_with_income = 0.0

            for purchase in company.purchases:
                quantity_shares += purchase.quantity
                total_amount += purchase.quantity * purchase.price
                actual_amount += purchase.quantity * shares_actual_price[company.asset]
            for income in company.incomes:
                total_income += income.value

            if quantity_shares != 0:
                avarage_price = total_amount / quantity_shares
                percentage = ((actual_amount - total_amount) / total_amount * 100) #((V2-V1)/V1 × 100)

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
