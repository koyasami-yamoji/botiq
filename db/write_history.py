import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import History


async def set_record_history(data: dict, session: AsyncSession) -> History:
	date_time = datetime.datetime.strptime(data['date_time'], '%d.%m.%Y %H:%M:%S')
	check_in = datetime.datetime.strptime(f"{data['CheckInDate']['year']}-{data['CheckInDate']['month']}-"
										  f"{data['CheckInDate']['day']}", "%Y-%m-%d")

	check_out = datetime.datetime.strptime(f"{data['CheckOutDate']['year']}-{data['CheckOutDate']['month']}-"
										  f"{data['CheckOutDate']['day']}", "%Y-%m-%d")
	record_history = History()
	record_history.user_id = data['chat_id']
	record_history.command = data['command']
	record_history.sort = data['sort']
	record_history.date_time = date_time
	record_history.count_photo = int(data['count_photo'])
	record_history.count_hotels = int(data['count_hotels'])
	record_history.destination_id = int(data['destination_id'])
	record_history.check_in = check_in
	record_history.check_out = check_out
	record_history.city = data['city']
	if data['command'] == '/custom':
		record_history.min_price = int(data['min_price'])
		record_history.max_price = int(data['max_price'])
		record_history.min_distance = int(data['min_distance'])
		record_history.max_distance = int(data['max_distance'])
	session.add(record_history)
	await session.commit()
	return record_history