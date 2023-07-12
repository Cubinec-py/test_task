from pydantic import EmailStr, BaseModel


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr | None = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr | None = None
    password: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
