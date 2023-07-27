# from typing import Callable, Awaitable, Dict, Any
#
# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject
# from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
#
#
# SESSION_POOL_KEY = "_session_pool"
# SESSION_KEY = "session"
#
#
# class DBSessionMiddleware(BaseMiddleware):
#     def __init__(
#         self,
#         pool_key: str = SESSION_POOL_KEY,
#         session_key: str = SESSION_KEY,
#     ) -> None:
#         self.pool_key = pool_key
#         self.session_key = session_key
#
#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: Dict[str, Any],
#     ) -> Any:
#         session_pool: async_sessionmaker[AsyncSession] = data[self.pool_key]
#
#         async with session_pool() as session:
#             data[self.session_key] = session
#             return await handler(event, data)