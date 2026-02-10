from app.extensions import db
from app.models import Users


def authenticate_user(valid_data):
    """Authenticate user credential"""

    user = Users.query.filter_by(username=valid_data.username).first()

    return user

