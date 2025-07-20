from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDatabase, UserList, UserResponse, UserSchema

app = FastAPI(title='MINHA API BALA!')
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserResponse)
def create_user(user: UserSchema):
    user_with_id = UserDatabase(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_user():
    return {
        'data': {'users': database},
        'pagination': {'page': 1, 'size': len(database), 'total': len(database), 'total_pages': 1},
    }


@app.get('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserResponse)
def read_user_by_id(user_id: int):
    print(f"database: {database}")
    print(f"user_id: {user_id}, acessando índice: {user_id - 1}")
    print(f"database: {database}")
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Usuário com ID {user_id} não encontrado.'
        )
    
    return database[user_id - 1]


@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserResponse)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDatabase(**user.model_dump(), id=user_id)

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Usuário com ID {user_id} não encontrado.'
        )
    database[user_id - 1] = user_with_id
    return user_with_id

@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Usuário com ID {user_id} não encontrado.'
        )
    database.pop(user_id - 1)
    return database
