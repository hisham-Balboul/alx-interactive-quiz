from flask_login import UserMixin
from extensions import db, bcrypt

class User(db.Model, UserMixin):
    """
    User model for storing user account details
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.first_name}', '{self.last_name}')"
    
    @staticmethod
    def add_user(username, first_name, last_name, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, first_name=first_name, last_name=last_name, password=hashed_password)
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    
