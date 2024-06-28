from extensions import db

class QuizQuestion(db.Model):
    """
    Model for storing quiz questions and their details
    """
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    option_1 = db.Column(db.String(100), nullable=False)
    option_2 = db.Column(db.String(100), nullable=False)
    option_3 = db.Column(db.String(100), nullable=False)
    option_4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"QuizQuestion('{self.question_text}', '{self.category}')"
    
    @staticmethod
    def add_question(question_text, option_1, option_2, option_3, option_4, correct_answer, category):
        question = QuizQuestion(
            question_text=question_text, 
            option_1=option_1, 
            option_2=option_2, 
            option_3=option_3, 
            option_4=option_4, 
            correct_answer=correct_answer, 
            category=category
        )
        db.session.add(question)
        db.session.commit()
    
    @staticmethod
    def get_categories():
        return QuizQuestion.query.with_entities(QuizQuestion.category).distinct().all()
    
    @staticmethod
    def get_questions_by_category(category):
        return QuizQuestion.query.filter_by(category=category).all()
