import json
from rdkit.Chem import AllChem as rdkit
mols = []
from rmm.models import Molecule, User, Score
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

with open('/Users/stevenbennett/Downloads/molder/database.json') as f:
        mols = json.loads(f.read())
list = list(mols.keys())

psql_url = 'postgresql://' + 'stevenbennett:@localhost/localdb'
db = create_engine(psql_url)
Session = sessionmaker(bind=db)
db_session = Session()

# Adding all molecules.
for inchi in list:
    mol = rdkit.MolToSmiles(rdkit.MolFromInchi(inchi), kekuleSmiles=False)
    molecule = Molecule(mol=mol)
    db_session.add(molecule)
db_session.commit()


# Adding Becky's molecules
smis = []
scores = []
molecule_ids = []
scores_keep = []

with open('/Users/stevenbennett/OneDrive - Imperial College London/PhD/Python Projects/MolderML/data/scores.csv') as file:
    read = csv.reader(file, delimiter=',')
    for row in read:
        smis.append(rdkit.MolToSmiles(rdkit.MolFromSmiles(row[0]), kekuleSmiles=False))
        scores.append(row[3])

becky = db_session.query(User).filter(User.username=='becky1').all()

len(scores)
len(smis)

for idx, molecule in enumerate(smis):
    # Gets molecule ID.
    mol = db_session.query(Molecule).filter(Molecule.mol==molecule).first()
    if mol:
        scores_keep.append(scores[idx])
        molecule_ids.append(mol.id)

len(scores_keep)
len(molecule_ids)

for idx, mol_id in enumerate(molecule_ids):
    molecule = db_session.query(Molecule).get(mol_id)
    becky.scores.append(Score(user=becky, molecule=molecule, sco=score))


db.session.rollback()
db.session.query(User).get(scores).any()
db.session.delete()
db.session.commit()
