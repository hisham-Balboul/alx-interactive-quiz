from flask import Blueprint, jsonify, request
from models import Leaderboard

bp = Blueprint('leaderboard_routes', __name__)

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
