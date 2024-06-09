import MySQLdb
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import JSON 
from .extensions import db



class User(UserMixin, db.Model):
    __tablename__ = 'users' 
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def is_active(self):
        return True 
    recipes = db.relationship('Recipe', back_populates='creator')



class Recipe(db.Model):
    __tablename__ = 'recipes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredients = db.Column(db.Text, nullable=False) 
    instructions = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', back_populates='recipes')





