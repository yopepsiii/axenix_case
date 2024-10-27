import asyncio

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


@celery_app.task()
def add_to_processing(*args):
    asyncio.run(make_order(*args))


async def make_order(order: dict):
    isOrderCompleted = False
    while not isOrderCompleted:
        await asyncio.sleep(3)
        departure_dates_str = '+'.join(order['departure_dates'])
        trains = await get_filtred_trains(startpoint=order['startpoint'],
                                          endpoint=order['endpoint'],
                                          wagons_types=order["wagon_type"],
                                          departure_dates=departure_dates_str)
        available_trains = list(filter(lambda train: train['available_seats_count'] >= order['ticket_count'], trains))

        # пока не успеваю с проверкой на предпочтительные места, они не учитываются в алгоритме

        if len(available_trains) > 0:
            for train in available_trains:
                wagons_ids = train['wagons_info']

                wagons = []
                for wagon_id in wagons_ids:
                    wagons.append(await send_httpx_request(url=f"{settings.case_api_url}/info/wagons/{wagon_id}",
                                                           request_type=RequestType.GET))
                for wagon in wagons:
                    wagon['seats'] = list(filter(lambda seat: seat['bookingStatus'] != 'BOOKED', wagon['seats']))
                    if len(wagon['seats']) > 0:
                        seat_ids = [seat.id for seat in wagon['seats']]

                        data = {
                            "train_id": train['id'],
                            "wagon_id": wagon['id'],
                            "seat_ids": seat_ids
                        }
                        isOrderCompleted = True
                        res = await send_httpx_request(url=f"{settings.case_api_url}/order",
                                                       data=data,
                                                       request_type=RequestType.POST)
