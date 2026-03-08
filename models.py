#  Модели данных (например, User)

from pydantic import BaseModel

# Модель пользователя
class User(BaseModel):
    username: str
    secret: str

