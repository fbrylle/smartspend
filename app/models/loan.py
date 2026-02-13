from app.extensions import db
from datetime import datetime


class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    # relationship
    payments = db.relationship('Payment', backref='debt', lazy=True, cascade="all, delete-orphan")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def remaining_balance(self):
        total_paid = sum(p.amount for p in self.payments)
        return self.total_amount - total_paid
