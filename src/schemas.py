from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserDB(UserPublic):
    id: int


class UserList(BaseModel):
    users: list[UserDB]
