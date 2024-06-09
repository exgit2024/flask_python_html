from flask import Flask
from .extensions import db, login_manager
from .main.routes import main_bp
from .auth.routes import auth_bp
# import MySQLdb

def create_app():
  # try:
  #     # Use MySQLdb to connect and create the database
  #     connection = MySQLdb.connect(host='localhost', user='root', password='Sql123###', db='test')
  #     cursor = connection.cursor()
  #     cursor.execute("CREATE DATABASE IF NOT EXISTS recipedb")
  #     cursor.close()
  #     connection.close()
  # except MySQLdb.Error as err:
  #     print(f"Error: {err}")

  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'your_secret_key'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sql123###@localhost/test'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Initialize extensions
  db.init_app(app)
  login_manager.init_app(app)

  # Register Blueprints
  app.register_blueprint(main_bp)
  app.register_blueprint(auth_bp)

  with app.app_context():
    db.create_all()

  return app
