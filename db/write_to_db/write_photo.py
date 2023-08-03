from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Photo


async def set_record_photo(images: list, hotel_id: int, session: AsyncSession) -> None:
    """
    Write photo to db
    :param session: AsyncSession
    :param images: list
    :param hotel_id: int
    :return: None
    """
    for one_photo in images:
        record_photo = Photo()
        record_photo.hotel_id = hotel_id
        record_photo.photo = one_photo
        session.add(record_photo)
    await session.commit()

