from app.models import Loan


def all_loan(current_user):
    loans = Loan.query.filter_by(user_id=current_user.id).all()
    return loans