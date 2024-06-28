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
with app.app_context():
        #db.create_all()  # Create tables if they don't exist

        # Add questions to the database if they don't already exist
        if QuizQuestion.query.count() == 59:
            for q in questions:
                QuizQuestion.add_question(
                    question_text=q["question_text"],
                    option_1=q["option_1"],
                    option_2=q["option_2"],
                    option_3=q["option_3"],
                    option_4=q["option_4"],
                    correct_answer=q["correct_answer"],
                    category=q["category"]
                )
            print("Questions added to the database.")
        else:
            quiz_questions = QuizQuestion.query.all()

# Print each quiz question for verification
            for question in quiz_questions:
                print(f"ID: {question.id}")
                print(f"Question Text: {question.question_text}")
                print(f"Options: {question.option_1}, {question.option_2}, {question.option_3}, {question.option_4}")
                print(f"Correct Answer: {question.correct_answer}")
                print(f"Category: {question.category}")
                print("-" * 20)

if __name__ == '__main__':
    app.run(debug=True)
