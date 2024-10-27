FROM python:3.12-alpine

WORKDIR /usr/src/AxenixCase/backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD sh -c "uvicorn main:app --host 0.0.0.0 --port 8000 --reload & celery -A task_queue.celery_app worker --loglevel=info"
