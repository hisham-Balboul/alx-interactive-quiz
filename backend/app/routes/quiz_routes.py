from flask import Blueprint, jsonify
from models import QuizQuestion

bp = Blueprint('quiz_routes', __name__)

@bp.route("/api/categories", methods=['GET'])
def get_categories():
    """
    API endpoint to get quiz categories
    """
    categories = QuizQuestion.get_categories()
    return jsonify([category[0] for category in categories])

@bp.route("/api/questions/<category>", methods=['GET'])
def get_questions(category):
    """
    API endpoint to get quiz questions by category
    """
    questions = QuizQuestion.get_questions_by_category(category)
    question_list = []
    for question in questions:
        question_data = {
            'question_text': question.question_text,
            'options': [question.option_1, question.option_2, question.option_3, question.option_4],
            'correct_answer': question.correct_answer
        }
        question_list.append(question_data)
    return jsonify(question_list)
