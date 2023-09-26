# Import Flask
from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Database config
    #need to fix the password before starting
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    @app.route('/')
    def hello():
        return 'Hello, PetFax'
    
    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    from . import modles
    modles.db.init_app(app)
    migrate = Migrate(app, modles.db)
    
    # return the app 
    return app