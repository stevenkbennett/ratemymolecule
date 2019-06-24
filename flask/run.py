from app import create_app, db
from app import cli

app = create_app()


if __name__=='__main__':
    app.run() 