import time

from fastapi import APIRouter, HTTPException
from starlette import status

from schemas.order import OrderInfo

from task_queue.celery_app import add_to_processing

from schemas.order import OrderStatus

router = APIRouter(prefix='/orders', tags=['Заказы'])


@router.post('/json', status_code=status.HTTP_201_CREATED, summary='Создать брони из JSON')
async def create_order_from_json(orders: list[OrderInfo]):
    for order in orders:
        res = add_to_processing.delay(order.dict(exclude_unset=True))

    return {'message': 'Запрос успешно принят к обработке. 💫'}

# @router.post('/', status_code=status.HTTP_201_CREATED, summary='Попытаться создать новую бронь')
# async def create_order():
#     pass
