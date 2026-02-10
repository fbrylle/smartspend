from app.models import Expense
from sqlalchemy import func
from app.extensions import db
from datetime import datetime


def get_expense_data():
    
    expenses = Expense.query.all()
    return expenses


def get_total_expenses(current_user):

    total = db.session.query(func.sum(Expense.amount)).filter(Expense.user_id == current_user.id).scalar() or 0

    return total


def get_daily_expense(current_user):
    now = datetime.now()

    day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    daily_spent = db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        Expense.created_at >= day_start
    ).scalar() or 0

    return daily_spent


def get_monthly_expense(current_user):
    now = datetime.now()

    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_spent = db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        Expense.created_at >= month_start
    ).scalar() or 0

    return monthly_spent


def get_expense_data_by_id(id, current_user):

    expense = Expense.query.filter_by(id=id, user_id=current_user)
    return expense