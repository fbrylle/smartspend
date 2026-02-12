from app.extensions import db
from app.models import Category, Expense



def delete_category_by_id(category_id, current_user):
    """Delete Category"""

    try:
        category = Category.query.filter_by(id=category_id, user_id=current_user).first_or_404()
        if category:
            db.session.delete(category)
            db.session.commit()
            return True, 'Successfully deleted a category and all the expenses under it.'
    except Exception as e:
        db.session.rollback()
        return False, "An error occured."
    

def delete_expense_by_id(category_id, expense_id, current_user):
    """ Delete expense """

    try:
        expense = Expense.query.filter_by(category_id=category_id, id=expense_id, user_id=current_user).first()
        if not expense:
            return False, 'Expense not found or unauthorized.'
        db.session.delete(expense)
        db.session.commit()
        return True, 'Successfully deleted an expense.'
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, f"{e}"
    

