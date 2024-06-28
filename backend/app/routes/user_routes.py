from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from models import User
import json

bp = Blueprint('user_routes', __name__)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    """
    Route for user registration
    """
    if current_user.is_authenticated:
        return jsonify({"message": "Already logged in"}), 200
    
    data = request.get_json()
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')

    if not username or not first_name or not last_name or not password:
        return jsonify({"message": "Missing fields"}), 400

    User.add_user(username, first_name, last_name, password)
    return jsonify({"message": "User registered successfully"}), 201

@bp.route("/login", methods=['GET', 'POST'])
def login():
    """
    Route for user login
    """
    if current_user.is_authenticated:
        return jsonify({"message": "Already logged in"}), 200
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_user_by_username(username)
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@bp.route("/logout", methods=['POST'])
def logout():
    """
    Route for user logout
    """
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
