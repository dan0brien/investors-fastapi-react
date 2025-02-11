from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'sqlite:///./data.db'


engine = create_engine(URL_DATABASE, connect_args = {"check_same_thread": False})




SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()
# df.to_sql('investors', con=engine, if_exists='replace', index=False)
