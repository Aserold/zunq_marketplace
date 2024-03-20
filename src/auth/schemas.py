from typing import Optional

from pydantic import EmailStr, ConfigDict

from fastapi_users import schemas

from fastapi_users.schemas import PYDANTIC_V2

from .models import UserType


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    status: UserType
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True, use_enum_values=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True
            use_enum_values = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    status: UserType
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

