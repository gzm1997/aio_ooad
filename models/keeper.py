import sqlalchemy as sa
from models.meta import meta
from passlib.hash import pbkdf2_sha256

keeper = sa.Table(
    "keeper",
    meta,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False, unique=True),
    sa.Column("psw_hash", sa.String(200), nullable=False)
)

async def insert(engine, keeper_object):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            psw_hash = pbkdf2_sha256.hash(keeper_object["psw"])
            await conn.execute(keeper.insert().values(name=keeper_object["name"], psw_hash=psw_hash))
            await trans.commit()
    except Exception as e:
        return e
    else:
        return True

async def delete(engine, id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(keeper.delete().where(keeper.c.id == id))
            await trans.commit()
    except:
        return False
    else:
        return True


async def select(engine, id = None, name = None):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        select_object = keeper.select()
        if id:
            select_object = select_object.where(keeper.c.id == id)
        if name:
            select_object == select_object.where(keeper.c.name == name)
        cursor = await conn.execute(select_object)
        records = await cursor.fetchall()
        await trans.commit()
        return [dict(r) for r in records]

async def verify(engine, name = None, psw = None):
    if not name or not psw:
        return False
    # try:
    async with engine.acquire() as conn:
        trans = await conn.begin()
        cursor = await conn.execute(keeper.select().where(keeper.c.name == name))
        record = await cursor.fetchone()
        # print("record", record)
        await trans.commit()
        if not record:
            return False
        psw_hash = dict(record)["psw_hash"]
        return pbkdf2_sha256.verify(psw, psw_hash)
    # except:
    #     return None
    # else:
    #     return result
