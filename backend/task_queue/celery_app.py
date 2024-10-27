import asyncio
import time

from celery import Celery

from config import settings
from schemas.order import OrderInfo

from routers.info import get_filtred_trains

from utils import send_httpx_request

from enums import RequestType

celery_app = Celery('tasks', broker=f'redis://'
                                    f'{settings.redis_host}:'
                                    f'{settings.redis_port}'
                                    f'/0')


@celery_app.task(rate_limit='40/h')
def add_to_processing(*args):
    asyncio.run(make_order(*args))


async def make_order(order: dict):
    isOrderCompleted = False
    while not isOrderCompleted:
        await asyncio.sleep(5)
        print('\n\n\nПолучаю информацию из API AxTrain по поездам...\n\n\n')
        departure_dates_str = '+'.join(order['departure_dates'])
        trains = await get_filtred_trains(startpoint=order['startpoint'],
                                          endpoint=order['endpoint'],
                                          wagons_types=order['wagon_type'],
                                          departure_dates=departure_dates_str)
        available_trains = list(filter(lambda train: train['available_seats_count'] >= order['ticket_count'], trains))

        # пока не успеваю с проверкой на предпочтительные места, они не учитываются в алгоритме

        if len(available_trains) > 0:
            print('\n\nНашелся нужный вам поезд, начинаю поиск по вагонам...\n\n')
            for train in available_trains:
                wagons_ids = train['wagons_info']
                wagons = []
                for wagon_id in wagons_ids:
                    wagons.append(await send_httpx_request(url=f"{settings.case_api_url}/info/wagons/{wagon_id}",
                                                           request_type=RequestType.GET))
                for wagon in wagons:
                    wagon['seats'] = list(filter(lambda seat: seat['bookingStatus'] != 'BOOKED', wagon['seats']))
                    if len(wagon['seats']) >= order['ticket_count']:
                        print('\n\nМы нашли места в вагоне, выбираем места...\n\n')
                        seat_ids = []

                        for seat in wagon['seats']:
                            if len(seat_ids) < order['ticket_count']:
                                seat_ids.append(seat['id'])
                            else:
                                break

                        data = {
                            "train_id": train['id'],
                            "wagon_id": wagon['id'],
                            "seat_ids": seat_ids
                        }
                        print('\n\nУра! Мы нашли нужный вам билет(ы), сейчас забронируем...\n\n')
                        isOrderCompleted = True
                        res = await send_httpx_request(url=f"{settings.case_api_url}/order",
                                                       data=data,
                                                       request_type=RequestType.POST)

                        print(f'\n\nИтог попытки забронировать: {res}\n\n')
