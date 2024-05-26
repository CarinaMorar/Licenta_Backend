from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.model.models import db

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/pet_feeder_db'   #aici partea de baza de date postgres
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from application.model import models

    db.init_app(app)
    with app.app_context():
        db.create_all()


    #urmeaza partea de controler aici si partea de CORS



    return app



