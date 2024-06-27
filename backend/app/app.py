from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample categories
categories = [
    {"id": 1, "name": "General Knowledge", "description": "Test your general knowledge."},
    {"id": 2, "name": "Science", "description": "Explore scientific facts and concepts."},
    # Add more categories here
]

# Sample questions
questions = {
    1: [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "correctAnswer": "Paris"},
        # Add more questions for General Knowledge here
    ],
    2: [
        {"question": "What is the boiling point of water?", "options": ["100°C", "90°C", "80°C", "70°C"], "correctAnswer": "100°C"},
        # Add more questions for Science here
    ]
}

@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/api/questions/<int:category_id>', methods=['GET'])
def get_questions(category_id):
    return jsonify(questions.get(category_id, []))

if __name__ == '__main__':
    app.run(debug=True)
