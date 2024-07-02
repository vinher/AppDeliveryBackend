from flask import Flask
from src.routes.home_page import *
from src.config import Config
from src.models import db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	jwt = JWTManager(app)
	db.init_app(app)

	app.route('/', methods=['GET'])(home_page)
	app.route('/register/user', methods=['POST'])(registerUser)
	app.route('/login', methods=['POST'])(login_user)
	
	return app

if __name__ == '__main__':
	app = create_app()
	app.run(host= '0.0.0.0',port=5001, debug = True)
