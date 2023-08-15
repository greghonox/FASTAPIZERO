from fastapi import FastAPI, HTTPException

from .schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Olá Mundo!'}


database = []  # provisório para estudo!


@app.post('/users/', status_code=201, response_model=UserPublic)
async def create_user(user: UserSchema) -> UserPublic:
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=200, response_model=UserList)
async def get_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
async def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]

    return {'detail': 'User deleted'}
