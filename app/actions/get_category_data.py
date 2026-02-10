from app.models import Category


def get_category_data(current_user):

    categories = Category.query.filter_by(user_id=current_user.id).all()

    return categories

def get_category_data_by_name(name, current_user):

    category = Category.query.filter_by(name=name, user_id=current_user.id).first_or_404()
    return category


def get_category_data_by_id(id, current_user):
    category = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    return category
