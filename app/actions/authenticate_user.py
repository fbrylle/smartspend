from app.extensions import db
from app.models import Users



def authenticate_user(form_data):
    """Authenticate user credential"""
    
    user = Users.query.filter_by(username=form_data.username).first()
    return user


