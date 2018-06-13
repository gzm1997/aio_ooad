import sqlalchemy as sa
from models.meta import meta

comment = sa.Table(
    "comment", 
    meta,
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("content", sa.String(50), nullable = False),
    sa.Column("food_id", sa.Integer, sa.ForeignKey("food.id"))
)


async def insert(engine, comment_object):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(comment.insert().values(id = comment_object["id"], content = comment_object["content"], food_id = comment_object["food_id"]))
            await trans.commit()
    except:
        return False
    else:
        return True


async def delete(engine, id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(comment.delete().where(id == id))
            await trans.commit()
    except:
        return False
    else:
        return True


async def select(engine, id = None, food_id = None):
    if not id and not food_id:
        return None
    async with engine.acquire() as conn:
        trans = await conn.begin()
        if id and food_id:
            cursor = await conn.execute(comment.select().where(id = id).where(food_id = food_id))
        elif not id and food_id:
            cursor = await conn.execute(comment.select().where(food_id = food_id))
        elif id and not food_id:
            cursor = await conn.execute(comment.select().where(id = id))
        records = cursor.fetchall()
        return [dict(r) for r in records]