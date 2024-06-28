from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from extensions import db, bcrypt, login_manager


load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'user_routes.login'  # Ensure you have a login route

    from models import User, QuizQuestion, Leaderboard

    from routes import user_routes, quiz_routes, leaderboard_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(quiz_routes.bp)
    app.register_blueprint(leaderboard_routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
