from fastapi import FastAPI, Path
from typing import Annotated

main_app = FastAPI()


@main_app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@main_app.get("/user/admin")
async def wel_adm() -> dict:
    return {"message": "Вы вошли как администратор"}


@main_app.get("/user/{username}/{age}")
async def usr_info(username: Annotated[str,Path(min_length=5, max_length=20, description="Enter username", example="Rinat")],
                   age: Annotated[int,Path(ge=18, le=120, description='Enter age', example="42")]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@main_app.get("/user/{user_id}")
async def wel_usr(user_id: int = Path(ge=1, le=100, description='Enter User ID', example="35")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
