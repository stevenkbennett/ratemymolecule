from rmm import db
from rmm import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from time import time
import jwt
from rmm import app
from sqlalchemy.ext.associationproxy import association_proxy

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    experience = db.Column(db.Integer)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # From the user in the database should be able to access the scores of the user and by extension
    # the molecules that have been scored.

    scores = db.relationship('Score', backref='user')

    def get_reset_password_token(self, expires_in=3600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
        
    def score_mol(self, score, molecule_id):
        # Score molecule takes input of the score and the molecule_id and appends the score to a user.
        molecule = db.session.query(Molecule).get(molecule_id)
        self.scores.append(Score(user=self, molecule=molecule, sco=score))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Molecule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mol = db.Column(db.String(200))

    # From the molecule should be able to access the scores of the molecule and the users by extension of the scores
    # The backref will generate a link to scores from the link to scores
    scores = db.relationship('Score', backref='molecule')

    def __repr__(self):
        return '<Smiles {}>'.format(self.mol)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sco = db.Column(db.Integer)

    # id for both the user that created the score and the molecule that is being scored.
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    mol_id = db.Column(db.Integer, db.ForeignKey(Molecule.id))


    def __repr__(self):
        return '<Score {}>'.format(self.mol_id)
