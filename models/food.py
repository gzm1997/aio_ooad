import sqlalchemy as sa
from models.meta import meta


food = sa.Table(
    "food",
    meta,
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("name", sa.String(50), unique = True, nullable = False),
    sa.Column("picture", sa.String(200)),
    sa.Column("price", sa.Integer, nullable = False),
    sa.Column("description", sa.String(50)),
    sa.Column("rating", sa.Float),
    sa.Column("amount", sa.Integer, nullable = False),
    sa.Column("likes", sa.Integer, default = 0),
    sa.Column("tag_id", sa.Integer, sa.ForeignKey("tag.id"), nullable = False)
)

async def insert(engine, food_object):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(food.insert().values(name = food_object["name"], picture = food_object["picture"], price = food_object["price"], description = food_object["description"], rating = food_object["rating"], amount = food_object["amount"], likes = 0, tag_id = food_object["tag_id"]))
            await trans.commit()
    except Exception as e:
        return e
    else:
        return True



async def delete(engine, food_id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(food.delete().where(food.c.id == food_id))
            await trans.commit()
    except:
        return False
    else:
        return True



async def select(engine, food_name = None, food_id = None, likes = None):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        select_object = food.select()
        if food_name:
            select_object = select_object.where(food.c.name == food_name)
        if food_id:
            select_object = select_object.where(food.c.id == food_id)
        if likes:
            select_object = select_object.where(food.c.likes >= likes)
        cursor = await conn.execute(select_object)
        records = await cursor.fetchall()
        await trans.commit()
        return [dict(r) for r in records]

async def like(engine, id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(food.update().where(food.c.id == id).values(likes = food.c.likes + 1))
            await trans.commit()
    except:
        return False
    else:
        return True





