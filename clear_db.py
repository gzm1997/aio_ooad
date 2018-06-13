from models.meta import meta
from models.tag import tag
from models.food import food
from models.comment import comment
from models.reservation import reservation
from models.keeper import keeper
from aiohttp_polls.setting import config
import sqlalchemy as sa
config = config["mysql"]

def drop_db():
    try:
        URI = "mysql+{connector}://{user}:{password}@{host}:{port}/{database}"
        URI = URI.format(
            connector=config["init_connector"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"],
            database=config["database"]
        )
        engine = sa.create_engine(URI)
        meta.drop_all(bind=engine)
    except Exception as e:
        return False
    else:
        return True

if __name__ == "__main__":
    print(drop_db())




