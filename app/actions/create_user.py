from app.extensions import db
from app.models import Users
from pydantic import ValidationError


def create_new_user(valid_data):
    """ Save new user to db """

    try:
        new_user = Users( 
                username = valid_data.username.lower(),
                fname=valid_data.fname,
                lname = valid_data.lname,
                password = valid_data.password.get_secret_value()
            )
        db.session.add(new_user)
        db.session.commit()
        return True, 'Successfully created a new user'
    except Exception as e:
        db.session.rollback()
        return False, 'An error occurred while creating a user.'