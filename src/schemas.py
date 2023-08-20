from pydantic import BaseModel, EmailStr, ConfigDict


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserDB(UserPublic):
    id: int


class UserList(BaseModel):
    users: list[UserDB]


class Message(BaseModel):
    detail: str
