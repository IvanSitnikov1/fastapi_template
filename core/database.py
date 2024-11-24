# from typing import AsyncGenerator
#
# from sqlalchemy import MetaData
# from sqlalchemy.ext.asyncio import (
#     AsyncSession, async_sessionmaker, create_async_engine)
# from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, \
#     mapped_column
#
# from .config import settings
#
#
# DATABASE_URL = (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}"
#                 f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
#
#
# class Base(DeclarativeBase):
#     __abstract__ = True
#
#     @declared_attr.directive
#     def __tablename__(cls) -> str:
#         return f"{cls.__name__.lower()}s"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#
# metadata = MetaData()
#
# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
