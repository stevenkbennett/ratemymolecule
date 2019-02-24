import unittest
from rmm import db, app
from rmm.models import User,Score,Molecule
from sqlalchemy.sql import null

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_score(self):
        u1 = User(username='bob', email='bob@bob.com')
        u2 = User(username='tom', email='tom@tom.com')

        db.session.add_all([u1, u2])
        db.session.commit()

        m1 = Molecule(mol='c1ccccc1')
        m2 = Molecule(mol='c1cccc1')
        m3 = Molecule(mol='c1ccc1')

        db.session.add_all([m1, m2, m3])
        db.session.commit()

        # Create four scores for molecules
        sco1 = Score(sco=1, mol_id=m1.id, user_id=u1.id)
        sco2 = Score(sco=0, mol_id=m2.id, user_id=u2.id)
        sco3 = Score(sco=1, mol_id=m3.id, user_id=u1.id)
        sco4 = Score(sco=0, mol_id=m1.id, user_id=u2.id)

        db.session.add_all([sco1, sco2, sco3, sco4])
        db.session.commit()

        u1.score(sco1, m1)
        u1.score(sco3, m1)
        u2.score(sco2, m1)
        u2.score(sco3, m1)
        db.session.commit()






if __name__=='__main__':
    unittest.main(verbosity=2)

# Random tests

db.session.query(Molecule).all()
db.session.query(User).all()

user.molecules.append(score2)
mol.users.append(score2)


mol = Molecule.query.get(5)

user = db.session.query(User).get(3)
user.scores

# Want to score molecule 5 and synthesisable
user2.score_mol(1, 3)
db.session.commit()

db.session.delete(score2)
db.session.add(score2)
db.session.commit()
score2.user
score2.molecule
db.session.dirty
db.session.query(Score.id).all()
db.session.rollback()
