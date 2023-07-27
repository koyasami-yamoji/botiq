from sqlalchemy.orm import declarative_base, sessionmaker
from config_data.config import user_name, password, host, port, db_name
from sqlalchemy import create_engine


engine = create_engine(f"postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db_name}")

Session_ = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
	Base.metadata.create_all(engine)
	return Session_()