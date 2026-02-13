from app.extensions import db
from app.models import Category
from app.schemas import CategoryUpdateSchema
from pydantic import ValidationError



def edit_category_name(category_id, user_id, formdata):
    """ Edit Category """

    category = Category.query.filter_by(id=category_id, user_id=user_id).first()
    if not category:
        return False, 'Category not found or unauthorized'
    
    
    try:
        validated_data = CategoryUpdateSchema(**formdata)
    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        return False, f"{error_msg}"
    try:
        new_name = validated_data.name
        existing = Category.query.filter_by(user_id=user_id, name=new_name).first()
        if existing and existing.id != category_id:
            return False, f"Category name already exist."
        
        category.name = new_name
        db.session.commit()
        return True, "Category Updated Successfully"
    except Exception as e:
        db.session.rollback()
        return False, 'Internal error occurred. Contact the developer.'