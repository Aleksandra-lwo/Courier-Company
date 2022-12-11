from fastapi import FastAPI
from routers import users, orders

app = FastAPI()

app.include_router(users.router)
app.include_router(orders.router)


@app.get('/api/v1')
async def root():
    return {
        "message": "Hello and Welcome to my application"
    }



