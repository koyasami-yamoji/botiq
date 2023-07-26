from config_data.config import user_name, password, host, port, db_name


def create_connect_db():
	result = f"postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db_name}"
	return result