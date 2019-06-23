from app import create_app

# Creates the app.
app = create_app()

# Runs RateMyMolecule.
if __name__ == '__main__':
    app.run()
