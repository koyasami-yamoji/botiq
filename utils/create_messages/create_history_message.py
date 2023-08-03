from db.models import History


def history_message(record: History):
    string = f"Дата и время запроса - {record.date_time}\n" \
            f"Город - {record.city}\n" \
            f"Введенная команда - {record.command}\n" \
            f"Дата заезда и выезда - {record.check_in} - {record.check_out}\n" \
            f"Количество отелей - {record.count_hotels}\n" \
            f"Количество фотографий - {record.count_photo}\n"
    if record.command == 'higher':
        string += f"Минимальная и максимальная цена - {record.min_price} - {record.max_price}\n"
        f"Минимальное и максимальное расстояние до центра - {record.max_distance} - {record.min_distance}\n"
    return string