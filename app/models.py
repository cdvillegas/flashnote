from app import db

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    cards = db.Column(db.Text, nullable=False)