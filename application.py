import asyncio
import aiohttp
from more_itertools import chunked
from lib.HeroClass import Hero, Base
from lib.settings import API_URL, db_engine, db_session, ALL_IDS, PARTITION

# проверка миграций
Base.metadata.create_all(db_engine)


async def get_hero(id, session):
    async with session.get(f'{API_URL}{id}') as response_data:
        try:
            if response_data.status == 200:
                JSON = await response_data.json()
                JSON['id'] = id
                JSON['films'] = ', '.join(JSON['films'])
                JSON['species'] = ', '.join(JSON['species'])
                JSON['starships'] = ', '.join(JSON['starships'])
                JSON['vehicles'] = ', '.join(JSON['vehicles'])
                return JSON

        except Exception as error:
            print(f'request error: {error}')


async def heroes_gen(all_ids, partition, session):
    for chank_ids in chunked(all_ids, partition):
        tasks = [asyncio.create_task(get_hero(hero_id, session)) for hero_id in chank_ids]
        for task in tasks:
            yield await task


async def write_hero():
    # открываем сессию для записи в БД
    db_write = db_session()
    async with aiohttp.ClientSession() as session:
        async for hero_pesrone in heroes_gen(ALL_IDS, PARTITION, session):

            try:
                new_hero = Hero(
                    id=hero_pesrone['id'],
                    name=hero_pesrone['name'],
                    birth_year=hero_pesrone['birth_year'],
                    eye_color=hero_pesrone['eye_color'],
                    films=hero_pesrone['films'],
                    gender=hero_pesrone['gender'],
                    hair_color=hero_pesrone['hair_color'],
                    height=hero_pesrone['height'],
                    homeworld=hero_pesrone['homeworld'],
                    mass=hero_pesrone['mass'],
                    skin_color=hero_pesrone['skin_color'],
                    species=hero_pesrone['species'],
                    starships=hero_pesrone['starships'],
                    vehicles=hero_pesrone['vehicles']
                )

                db_write.add(new_hero)
                db_write.commit()
                print(f'hero "{hero_pesrone["name"]}" with id={hero_pesrone["id"]} was successfully added to the database')
            except Exception as err:
                print(f'\nresponse error: {err}\n')

    db_write.close()


asyncio.run(write_hero())
