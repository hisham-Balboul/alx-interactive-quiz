from flask import Blueprint, jsonify, request
from models import Leaderboard

bp = Blueprint('leaderboard_routes', __name__)

@bp.route("/api/leaderboard", methods=['POST'])
def add_leaderboard_entry():
    """
    API endpoint to add a new leaderboard entry
    """
    data = request.get_json()
    username = data['username']
    score = data['score']
    category = data['category']
    
    Leaderboard.add_entry(username, score, category)
    return jsonify({"message": "Entry added successfully"}), 201

@bp.route("/api/leaderboard/<category>", methods=['GET'])
def get_leaderboard(category):
    """
    API endpoint to get the leaderboard for a specific category
    """
    leaderboard = Leaderboard.get_leaderboard_by_category(category)
    leaderboard_list = [{
        'username': entry.username,
        'score': entry.score,
        'category': entry.category,
        'date': entry.date.strftime('%Y-%m-%d %H:%M:%S')
    } for entry in leaderboard]
    return jsonify(leaderboard_list)

@bp.route("/api/leaderboard/categories", methods=['GET'])
def get_categories():
    """
    API endpoint to get all unique leaderboard categories
    """
    categories = Leaderboard.get_categories()
    category_list = [category[0] for category in categories]  # Extract category names from tuples
    return jsonify(category_list)

@bp.route('/delete_leaderboard_entries', methods=['POST'])
def delete_leaderboard_entries():
    try:
        num_deleted = Leaderboard.remove_all_entries()
        return jsonify({"message": f"Successfully deleted {num_deleted} entries from the leaderboard."}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to delete leaderboard entries: {str(e)}"}), 500
