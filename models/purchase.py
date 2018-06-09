from db import db
from datetime import datetime

class PurchaseModel(db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(precision=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.DateTime(timezone=True), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('CompanyModel')

    def __init__(self, price, quantity, company_id, purchase_date):
        self.price = price
        self.quantity = quantity
        self.company_id = company_id
        self.purchase_date = purchase_date

    def json(self):
        if self.purchase_date is None:
            purchase_date_out = None
        else:
            purchase_date_out = datetime.strftime(self.purchase_date, "%Y-%m-%d")

        return {'price': self.price, 'quantity': self.quantity, 'purchase_date': purchase_date_out}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()