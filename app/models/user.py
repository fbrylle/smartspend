from app.extensions import db, bcrypt, login_manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), nullable=False, unique=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    # relationship
    categories = db.relationship('Category', backref='owner', lazy=True)
    expenses = db.relationship('Expense', backref='author', lazy=True, cascade="all, delete-orphan")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))