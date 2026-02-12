from app.extensions import db
from sqlalchemy import UniqueConstraint


class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    expenses = db.relationship('Expense', backref='owner', lazy=True, cascade="all, delete-orphan")

    
    __table_args__ = (
        UniqueConstraint('name', 'user_id', name='_user_category_uc'),
    )