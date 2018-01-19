from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("Application")
# On configure la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://gazetteer_user:password@localhost/gazetteer'
# On initie l'extension
db = SQLAlchemy(app)

from .routes import lieu, accueil