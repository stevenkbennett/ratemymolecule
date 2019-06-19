
from models import Score, Molecule, User

from run import create_app, db
import cli

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Score': Score, 'Molecule': Molecule}

if __name__=='__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
    )