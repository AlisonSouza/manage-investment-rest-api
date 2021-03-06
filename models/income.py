from db import db
from datetime import datetime

class IncomeModel(db.Model):
    __tablename__ = 'income'

    id = db.Column(db.Integer, primary_key=True)
    receive_date = db.Column(db.DateTime(timezone=True), nullable=False)
    value = db.Column(db.Float(precision=2), nullable=False)
    income_type = db.Column(db.String(3), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('CompanyModel')

    def __init__(self, value, income_type, company_id, receive_date):
        self.receive_date = receive_date
        self.value = value
        self.income_type = income_type
        self.company_id = company_id

    def json(self):
        if self.receive_date is None:
            receive_date_out = None
        else:
            receive_date_out = datetime.strftime(self.receive_date, "%Y-%m-%d")

        return {'value': self.value, 'income_type': self.income_type, 'receive_date': receive_date_out}

    def save(self):
        db.session.add(self)
        db.session.commit()