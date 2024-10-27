from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import order, info

app = FastAPI(root_path='/api/v1')

app.include_router(order.router)
app.include_router(info.router)

app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=[''])