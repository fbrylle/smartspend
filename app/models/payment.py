from app.extensions import db
from datetime import datetime


class Payment(db.Model):
    __tablename__='payments'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.now)
    
    # relationship
    debt_id = db.Column(db.Integer, db.ForeignKey('loans.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)