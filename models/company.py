from db import db

class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    asset = db.Column(db.String(80))

    purchases = db.relationship('PurchaseModel', lazy='dynamic')
    incomes = db.relationship('IncomeModel', lazy='dynamic')

    def __init__(self, asset):
        self.asset = asset

    def json(self):
        return {'asset': self.asset, 
                'purchases': list(map(lambda x: x.json(), self.purchases.all())), 
                'incomes': list(map(lambda x: x.json(), self.incomes.all()))}

    @classmethod
    def find_by_name(cls, asset):
        return cls.query.filter_by(asset=asset).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
