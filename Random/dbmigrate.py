from rmm.models import User, Score, Molecule
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_urls = {'sqlite': 'sqlite:///app.db',
                 'mysql': 'mysql://steven:steven@localhost/rmm'}

sqlite = create_engine(database_urls['sqlite'])
mysql = create_engine(database_urls['mysql'])

mysql_session = sessionmaker(mysql)
sqlite_session = sessionmaker(sqlite)

mysql_session1 = mysql_session()
sqlite_session1 = sqlite_session()

users = sqlite_session1.query(User).all()
molecules = sqlite_session1.query(Molecule).all()
scores = sqlite_session1.query(Score).all()
len(scores)
mysql_session1.add_all(users)
