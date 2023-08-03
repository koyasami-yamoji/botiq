from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Row, RowMapping

from db.models import History


async def get_history_from_db(user_id, session: AsyncSession) -> Sequence[Row | RowMapping | Any]:
	history_request = await session.execute(select(History).where(History.user_id == user_id))
	return history_request.scalars().all()
