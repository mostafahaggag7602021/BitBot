from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../')
import localsettings


db_credential = localsettings.db_credential
engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(db_credential['username'],
                                                              db_credential['password'], localsettings.db_credential['host'],
                                                              db_credential['port'],
                                                              db_credential['dbname']
                                                              )
                       )
Session = sessionmaker(bind=engine)
