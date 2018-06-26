from models import reservation
from models import food
import datetime
import calendar
import ast

sales_food = food
sales_reservation = reservation

async def sales_permonth(engine, id = None):
    if not id:
        return None
    first_day_of_month = datetime.datetime.today().replace(day = 1)
    num_of_day_of_this_month = calendar.monthrange(first_day_of_month.year, first_day_of_month.month)[1]
    last_day_of_month = datetime.datetime.today().replace(day = num_of_day_of_this_month)
    async with engine.acquire() as conn:
        trans = await conn.begin()
        cursor = await conn.execute(reservation.reservation.select().where(reservation.reservation.c.reserve_datetime >= first_day_of_month).where(reservation.reservation.c.reserve_datetime <= last_day_of_month))
        reservations_result = await cursor.fetchall()
        reservations_result = [dict(r) for r in reservations_result]
        #print("reservation", reservations_result)
        await trans.commit()
        trans = await conn.begin()
        cursor = await conn.execute(food.food.select().where(food.food.c.id == id))
        food_name_result = await cursor.fetchone()
        food_name_result = dict(food_name_result)["name"]
        print("food_name", food_name_result)
        await trans.commit()
        count = 0
        for r in reservations_result:
            print("r", r["food_list"])
            print("type of foodlist", type(r["food_list"]))
            food_list = r["food_list"]
            print("type", type(food_list))
            print(food_list)
            if food_name_result in food_list.keys():
                count += food_list[food_name_result]
        return count


async def reservation_quantity_piedata(engine):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        cursor = await conn.execute(food.food.select())
        food_name = await cursor.fetchall()
        cursor = await conn.execute(reservation.reservation.select())
        food_lists = await cursor.fetchall()
        food_name = [dict(n)["name"] for n in food_name]
        food_lists = [dict(f)["food_list"] for f in food_lists]
        # print("food name", food_name, "food lists", food_lists)
        await trans.commit()
        r = []
        for fn in food_name:
            t = {
                "x": fn
            }
            count = 0
            for l in food_lists:
                if fn in l.keys():
                    count += l[fn]
            t["y"] = count
            r.append(t)
        return r


async def turnover_piedata(engine):
    async with engine.acquire() as conn:
        trans = await conn.begin()
        cursor = await conn.execute(food.food.select())
        food_name = await cursor.fetchall()
        cursor = await conn.execute(reservation.reservation.select())
        food_lists = await cursor.fetchall()
        foods = [dict(n) for n in food_name]
        food_lists = [dict(f)["food_list"] for f in food_lists]
        # print("food name", food_name, "food lists", food_lists)
        await trans.commit()
        r = []
        for f in foods:
            t = {
                "x": f["name"]
            }
            turnover = 0
            for l in food_lists:
                if f["name"] in l.keys():
                    turnover += l[f["name"]] * f["price"]
            t["y"] = turnover
            r.append(t)
        return r

