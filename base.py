from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

schema = 'movies'
engine = create_engine('postgresql+psycopg2://usr:pass@localhost:5432/sqlalchemy',
                       connect_args={'options': '-csearch_path={}'.format(schema)})
Session = sessionmaker(bind=engine)

Base = declarative_base()
