import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from .db_config import *


engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# När man skapar egna klasser använder man declarative_base
Base = declarative_base()
Session = sessionmaker()

# Engine är den delen som gör att vi kan prata med databasen.
Session.configure(bind=engine)
session = Session()





