from app.extensions import db
from pydantic import ValidationError
from app.models import Loan
from app.schemas import LoanSchema


def new_loan(current_user, form_data):
    """Add new loan save to db"""
    
    try:
        valid_data = LoanSchema(**form_data)
    except ValidationError as e:
        return False, f"{e.errors()[0]['msg']}"
    
    try:
        new_loan = Loan(
            name = valid_data.name,
            total_amount = valid_data.total_amount,
            user_id = current_user
        )
        db.session.add(new_loan)
        db.session.commit()
        return True, 'Successfully registered your loan.'
    except Exception as e:
        db.session.rollback()
        return False, 'An error occurred contact the developer.'