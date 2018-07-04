from flask_restful import Resource, Api, reqparse
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Sumaries(Resource):
    def get(self):
        companies = CompanyModel.query.all()
        sumaries = []
        shares_actual_price = {'EGIE3': 34.26, 
                            'ODPV3': 12.69,
                            'LREN3': 29.00,
                            'MDIA3': 37.47,
                            'MOVI3': 5.18,
                            'GRND3': 8.01,
                            'ARZZ3': 42.50,
                            'BBSE3': 24.40,
                            'FLRY3': 25.71,
                            'CIEL3': 16.20,
                            'SMLS3': 52.50,
                            'PSSA3': 39.80,
                            'WEGE3': 15.66,
                            'ITUB3': 35.78
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
                actual_amount_with_income += total_income + actual_amount
                actual_percentage_with_income = ((actual_amount_with_income - total_amount) / total_amount * 100) #((V2-V1)/V1 × 100)



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

            total_portifolio = 0
            total_portifolio_actual = 0
            for dto in sumaries:
                total_portifolio += dto.total_amount
                total_portifolio_actual += dto.actual_amount + dto.total_income
                
            

        return {'total_portifolio_actual': total_portifolio_actual, 'total_portifolio': total_portifolio, 'sumaries': [x.json() for x in sumaries]}

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
