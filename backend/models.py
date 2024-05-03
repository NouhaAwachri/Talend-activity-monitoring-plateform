from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Users(UserMixin, db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(45))


    def get_id(self):
        return str(self.userid)