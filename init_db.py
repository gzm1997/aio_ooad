from models.meta import meta
from models.tag import tag
from models.food import food
from models.comment import comment
from models.reservation import reservation
from models.keeper import keeper
from aiohttp_polls.setting import config
import sqlalchemy as sa

config = config["mysql"]
URI = "mysql+{connector}://{user}:{password}@{host}:{port}"
URI = URI.format(
    connector = config["init_connector"],
    user = config["user"],
    password = config["password"],
    host = config["host"],
    port = config["port"]
)
engine = sa.create_engine(URI)


#init_database函数用于flask运行之前同步初始化数据库，app的连接引擎是异步的，由aiomysql.ra提供连接
def init_database():
    try:
        with engine.connect() as conn:
            #print("conn", conn)
            conn.execute("create database if not exists restaurant;")
            conn.execute("use restaurant;")
        if not engine.dialect.has_table(engine, table_name="tag") and not engine.dialect.has_table(engine, table_name="food") and not engine.dialect.has_table(engine, table_name="comment") and not engine.dialect.has_table(engine, table_name="reservation") and not engine.dialect.has_table(engine, table_name="keeper"):
            meta.create_all(bind=engine, tables=[tag, food, comment, reservation, keeper])
    except:
        return False
    else:
        return True


if __name__ == "__main__":
    print(init_database())