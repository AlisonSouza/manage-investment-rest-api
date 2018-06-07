from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from resources.company import Company, CompanyList
from resources.purchase import Purchase, PurchaseList
from resources.user import UserRegister
from resources.sumaries import Sumaries
from resources.income import Income

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'alison'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Company, '/company/<string:name>')
api.add_resource(Purchase, '/purchase/<string:name>')
api.add_resource(CompanyList, '/companies')
api.add_resource(PurchaseList, '/purchases')
api.add_resource(UserRegister, '/register')
api.add_resource(Sumaries, '/sumaries')
api.add_resource(Income, '/income/<string:company_name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)