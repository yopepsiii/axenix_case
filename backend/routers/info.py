from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException

from config import settings
from enums import RequestType
from starlette import status
from utils import send_httpx_request

from typing import Optional

router = APIRouter(prefix='/info', tags=['Поезда'])


@router.get('/filtered_trains')
async def get_filtred_trains(startpoint: str,
                             endpoint: str,
                             departure_dates: str,
                             wagons_types: Optional[str] = None,
                             ):  # разделитель на список это +
    trains = await send_httpx_request(url=f'{settings.case_api_url}/info/trains',
                                      params={'booking_available': True,
                                              'start_point': startpoint,
                                              'end_point': endpoint},
                                      request_type=RequestType.GET)
    departure_dates_list = departure_dates.split('+')
    trains = list(filter(lambda train: train['startpoint_departure'][:10] in departure_dates_list, trains))

    if len(trains) > 0:

        if not wagons_types:
            return trains

        filtered_trains = []
        for train in trains:
            filtered_wagons = list(filter(lambda wagon: wagon['type'] in wagons_types, train['wagons_info']))

            if filtered_wagons:
                train['wagons_info'] = filtered_wagons
                filtered_trains.append(train)
        return filtered_trains
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='По вашему запросов поездов не найдено.')


@router.get('/trains/{train_id}/filtered_wagons')
async def list_wagons(
        train_id: int,
        price_range: Optional[str] = '',
        wagons_types: Optional[str] = None,
        block_type: Optional[str] = None
):
    wagons = await send_httpx_request(
        url=f'{settings.case_api_url}/info/wagons',
        params={'trainId': train_id},
        request_type=RequestType.GET
    )

    if len(wagons) > 0:

        if price_range:
            price = list(map(int, price_range.split('-')))
        else:
            price = [-1, 9999999999999]

        if wagons_types:
            # wagons = filter(lambda wagon: wagon['type'] in wagons_types, wagons)
            wagons = filter(lambda wagon: wagon['type'] in wagons_types, wagons)

        result = []

        for wagon in wagons:
            filtered_seats = list(filter(lambda seat: price[0] <= seat['price'] <= price[1], wagon['seats']))

            if block_type:
                filtered_seats = list(filter(lambda seat: seat['block'] == block_type, filtered_seats))

            if filtered_seats:
                wagon['seats'] = filtered_seats
                result.append(wagon)

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='По вашему запросов вагонов не найдено.')

    return result


@router.get('/wagons/{wagon_id}/filtered_seats')
async def get_seats(wagon_id: int,
                    price_range: Optional[str] = '',
                    block_type: Optional[str] = None,
                    bookingStatus: Optional[str] = None):
    seats = await send_httpx_request(
        url=f'{settings.case_api_url}/info/seats',
        params={'wagonId': wagon_id},
        request_type=RequestType.GET
    )

    if len(seats) > 0:
        if price_range:
            price = list(map(int, price_range.split('-')))
        else:
            price = [-1, 9999999999999]

        if block_type:
            seats = list(filter(lambda seat: seat['block'] == block_type, seats))
        if bookingStatus:
            seats = list(filter(lambda seat: seat['bookingStatus'] == bookingStatus, seats))

        seats = list(filter(lambda seat: price[0] <= seat['price'] <= price[1], seats))
        return seats

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='По вашему запросов мест не найдено.')
