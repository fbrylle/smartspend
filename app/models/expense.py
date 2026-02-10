from app.extensions import db
from datetime import datetime


class Expense(db.Model):
    __tablename__='expenses'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # relationship
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)