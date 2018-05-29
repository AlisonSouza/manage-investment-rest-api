from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.company import CompanyModel
from models.purchase import PurchaseModel

class Company(Resource):

    #@jwt_required()
    def get(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            return company.json()
        return {'message': 'Company not found'}, 404

    def post(self, name):
        if CompanyModel.find_by_name(name):
            return {'company': "a company with name '{}' already exist.".format(name)}, 400

        company = CompanyModel(name)

        try:
            company.save_to_db()
        except:
            return {"message": "An error occurred inserting the Company."}, 500
        
        return company.json(), 201

    def delete(self, name):
        company = CompanyModel.find_by_name(name)
        if company:
            company.delete_from_db()
        return {'message': 'Company deleted'}

    def put(self, name):
        data = Company.parser.parse_args()

        company = CompanyModel.find_by_name(name)

        if company is None:
            company = CompanModel(name, data['price'])
        else:
            company.price = data['price']
        company.save_to_db()
        return company.json()

class CompanyList(Resource):
    def get(self):
        return {'companies': [x.json() for x in CompanyModel.query.all()]}