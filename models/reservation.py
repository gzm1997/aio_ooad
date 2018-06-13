import sqlalchemy as sa
from models.meta import meta
import datetime

reservation = sa.Table(
    "reservation",
    meta,
    sa.Column("isPaid", sa.Boolean, default = False),
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("reserve_datetime", sa.DateTime),
    sa.Column("pay_datetime", sa.DateTime),
    sa.Column("table_num", sa.Integer, nullable = False),
    sa.Column("food_list", sa.JSON),
    sa.Column("total", sa.Float)
)


async def insert(engine, reservation_object):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        if "pay_datetime" not in reservation_object:
        	await conn.execute(reservation.insert().values(isPaid = reservation_object["isPaid"], reserve_datetime = datetime.datetime.now(), table_num = reservation_object["table_num"], food_list = reservation_object["food_list"], total = reservation_object["total"]))
        elif "pay_datetime" in reservation_object:
        	await conn.execute(reservation.insert().values(isPaid = reservation_object["isPaid"], reserve_datetime = datetime.datetime.now(), pay_datetime = reservation_object["pay_datetime"], table_num = reservation_object["table_num"], food_list = reservation_object["food_list"], total = reservation_object["total"]))
        cursor = await conn.execute("SELECT LAST_INSERT_ID() FROM reservation;")
        record = await cursor.fetchone()
        await trans.commit()
        return dict(record)



async def delete(engine, id):
    try:
        async with engine.acquire() as conn:
            trans = await conn.begin()
            await conn.execute(reservation.delete().where(id == id))
            await trans.commit()
    except:
        return False
    else:
        return True


async def select(engine, id = None, reserve_datetime = None, pay_datetime = None, table_num = None):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        select_object = reservation.select()
        if id:
            select_object = select_object.where(reservation.c.id == id)
        if reserve_datetime:
            select_object = select_object.where(reservation.c.reserve_datetime == reserve_datetime)
        if pay_datetime:
            select_object = select_object.where(reservation.c.pay_datetime == pay_datetime)
        if table_num:
            select_object = select_object.where(reservation.c.table_num == table_num)
        cursor = await conn.execute(select_object)
        records = await cursor.fetchall()
        await trans.commit()
        return [dict(r) for r in records]