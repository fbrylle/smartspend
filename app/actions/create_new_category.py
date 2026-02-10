from app.extensions import db
from app.models import Category
from app.schemas import CategorySchema


def create_new_category(current_user, form_data):
    """ Create new category and Save to db """

    valid_data = CategorySchema(**form_data)

    try:
        new_category = Category(
            name = valid_data.name,
            user_id = current_user.id
        )
        db.session.add(new_category)
        db.session.commit()
        return True, 'Successfully added a category.'
    except Exception as e:
        db.session.rollback()
        return False, 'An error occured. Contact the developer'

