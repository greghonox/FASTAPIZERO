from fastapi import FastAPI

from src.routers import auth, todos, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/')
async def read_root():
    return {'message': 'Olá Mundo!'}
