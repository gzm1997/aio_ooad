import sqlalchemy as sa
from models.meta import meta
import asyncio

tag = sa.Table(
    "tag", 
    meta,
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("description", sa.String(50)),
    sa.Column("picture", sa.String(50))
)


async def insert(engine, tag_object):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(tag.insert().values(description = tag_object["description"], picture = tag_object["picture"]))
            await trans.commit()
    except:
        return False
    else:
        return True



async def delete(engine, tag_id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(tag.delete().where(tag.c.id == tag_id))
            await trans.commit()
    except:
        return False
    else:
        return True



async def select(engine, tag_id):
    if not tag_id:
        return None
    async with engine.acquire() as conn:
        trans = await conn.begin()
        cursor = await conn.execute(tag.select().where(tag.c.id == tag_id))
        records = await cursor.fetchall()
        await trans.commit()
        return [dict(r) for r in records]



if __name__ == "__main__":
	pass