from flask import render_template, request, redirect
from app import app, db
from app.models import Deck
import json
import os

@app.route('/decks', methods=['GET', 'POST'])
def decks():
    if request.method == 'POST':
        # Extract data from the request
        title = request.form.get('title')
        description = request.form.get('description')
        cards = request.form.get('cards')

        # Add new record to database
        deck = Deck(title=title, description=description, cards=cards)
        db.session.add(deck)
        db.session.commit()

        return redirect(os.path.join('decks', str(deck.id)))

    # Query titles and descriptions of all decks
    decks = Deck.query.with_entities(Deck.title, Deck.description)

    return render_template('decks.html', decks=decks)

@app.route('/decks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def deck(id):
    # Get the deck
    deck = Deck.query.filter_by(id=id).first()

    if request.method == 'PUT':
        # Update record in the database
        deck.update({
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'cards': request.form.get('id'),
        })
        db.session.commit()
    elif request.method == 'DELETE': 
        # Delete from database and redirect
        db.session.delete(deck)
        db.session.commit()
        return redirect('/decks')

    # Unmarshal cards json string into dictionary
    [deck.update({'cards': json.loads(deck['cards'])}) for deck in decks]

    return str(deck)