def parse_result(parse_list: dict, data: dict) -> dict:
	hotels_data = {}
	if data['command'] in ['/lower', 'higher']:
		for hotel in parse_list:
			try:
				hotels_data[hotel['id']] = create_hotel_data(hotel)

			except (ValueError, TypeError):
				continue

		if data['command'] == '/higher':
			hotels_data = {
				key: value for key, value in sorted(hotels_data.items(),
													key=lambda hotel_id: hotel_id[1]['price'], reverse=True)
			}

	else:
		for hotel in parse_list:
			if float(data['min_distance']) < hotel['destinationInfo']['distanceFromDestination']['value'] * 1.61 < \
				float(data['max_distance']):
				hotels_data[hotel['id']] = create_hotel_data(hotel)

	return hotels_data


def create_hotel_data(hotel: dict) -> dict:
	hotel_data = {'name': hotel['name'], 'id': hotel['id'],
				  'distance': hotel['destinationInfo']['distanceFromDestination']['value'] * 1.61,
				  'unit': hotel['destinationInfo']['distanceFromDestination']['unit'],
				  'price': hotel['price']['lead']['amount'],
				  "user_rating": float(hotel['reviews']['total'])}

	return hotel_data
