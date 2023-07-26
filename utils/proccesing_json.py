import json


def get_cities(response_text):
	possible_cities = {}
	data = json.loads(response_text)
	if not data:
		raise LookupError('Запрос пуст')
	for id_place in data['sr']:
		try:
			possible_cities[id_place['gaiaId']] = {
				'gaiaId': id_place['gaiaId'],
				'regionNames': id_place['regionNames']['fullName']
			}
		except KeyError:
			continue
		return possible_cities