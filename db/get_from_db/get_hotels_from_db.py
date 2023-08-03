from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Row, RowMapping

from db.models import History, Hotels


async def get_hotels(history: History, session: AsyncSession):
	request_hotels = await session.execute(select(Hotels).where(Hotels.history_id == history.id))
	return request_hotels

