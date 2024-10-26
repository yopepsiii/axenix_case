from celery import Celery

from backend.config import settings

celery_app = Celery('tasks', broker=f'redis://'
                                    f'{settings.redis_host}:'
                                    f'{settings.redis_port}'
                                    f'/0')


@celery_app.task(name='check_tickets_avaliable')
def check_tickets_avaliable():
    pass
    # todo: прописать селери

