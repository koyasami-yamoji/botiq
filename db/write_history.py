from sqlalchemy.orm import Session
from db.models import History

import datetime


def set_history(data: dict, session: Session) -> History:
	record_history = History()
	record_history.user_id = data['chat_id']
	record_history.command = data['command']
	record_history.sort = data['sort']
	record_history.date_time = datetime.datetime.strptime(data['date_time'], '%d.%m.%Y %H:%M:%S')
	record_history.count_photo = data['count_photo']
	record_history.count_hotels = data['count_hotels']
	record_history.destination_id = data['destination_id']
	record_history.check_in_year = data['CheckInDate']['year']
	record_history.check_in_month = data['CheckInDate']['month']
	record_history.check_in_day = data['CheckInDate']['day']
	record_history.check_out_year = data['CheckOutDate']['year']
	record_history.check_out_month = data['CheckOutDate']['month']
	record_history.check_out_day = data['CheckOutDate']['day']
	record_history.city = data['city']
	if data['command'] == '/custom':
		record_history.min_price = data['min_price']
		record_history.max_price = data['max_price']
		record_history.min_distance = data['min_distance']
		record_history.max_distance = data['max_distance']
	session.add(record_history)
	session.commit()
	session.flush()
	return record_history