from rmm import create_app, db, cli
from rmm.models import User, Molecule, Score

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Score': Score, 'Molecule': Molecule}
