from datetime import datetime
from extensions import db

class Leaderboard(db.Model):
    """
    Model for storing leaderboard entries
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Leaderboard('{self.username}', '{self.score}', '{self.category}', '{self.date}')"
    
    @staticmethod
    def add_entry(username, score, category):
        """
        Add a new entry to the leaderboard
        """
        entry = Leaderboard(username=username, score=score, category=category)
        db.session.add(entry)
        db.session.commit()
    
    @staticmethod
    def get_leaderboard_by_category(category):
        """
        Get the leaderboard entries for a specific category
        """
        return Leaderboard.query.filter_by(category=category).order_by(Leaderboard.score.desc()).all()
