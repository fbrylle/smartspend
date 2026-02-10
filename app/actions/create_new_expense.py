from app.models import Expense, Category
from app.extensions import db
from app.schemas import ExpenseSchema


def create_new_expense(current_user, category_id, form_data):
    """Create new expense and Save to db"""

    valid_data = ExpenseSchema(**form_data)

    try:
        new_expense = Expense(
            amount = valid_data.amount,
            user_id = current_user.id,
            description = valid_data.description,
            category_id = category_id
        )
        db.session.add(new_expense)
        db.session.commit()
        return True, "Successfully added your expense"
    except Exception as e:
        db.session.rollback()
        return False, "An error occured, Contact the developer."
