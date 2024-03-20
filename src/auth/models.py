import enum
import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, TIMESTAMP, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from src.database import intpk


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class UserType(enum.Enum):
    BUYER = 'buyer'
    SELLER = 'seller'


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
        )
    username: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[UserType] = mapped_column(Enum(UserType), nullable=False)
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    registered_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, default=datetime.datetime.now(datetime.UTC)
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
