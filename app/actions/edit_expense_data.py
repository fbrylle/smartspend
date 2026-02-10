from app.extensions import db
from app.models import Expense
from app.schemas import UpdateExpenseSchema
from pydantic import ValidationError


def edit_expense_service(category_id, expense_id, user_id, form_data):
    """ Edit Expense Data """

    expense = Expense.query.filter_by(id=expense_id, category_id=category_id, user_id=user_id).first()
    if not expense:
        return False, "Expense not found or unauthorized."
    
    try:
        validated_data = UpdateExpenseSchema(**form_data)
        new_amount = validated_data.amount
        new_description = validated_data.description

        expense.amount = new_amount
        expense.description = new_description
        db.session.commit()
        return True, "Expense successfully updated."
    
    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        return False, f"Validation error: {error_msg}"
    except Exception as e:
        db.session.rollback()
        return False, 'Internal error occurred. Contact the developer.'