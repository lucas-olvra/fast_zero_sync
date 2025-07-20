from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDatabase(UserSchema):
    id: int


class UserContent(BaseModel):
    users: list[UserResponse]


class PaginationSchema(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int


class UserList(BaseModel):
    data: UserContent
    pagination: PaginationSchema
