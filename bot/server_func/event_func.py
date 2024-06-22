import requests

from .server_client import URL, auth


"""
Функции для callback-запроса.
Получает ключ в виде даты(мм-дд) и возвращает уже отсортированный список в событиями
"""


async def event_request(date_key: str):
    url_event = URL + "event/2025-" + date_key[3:] + "-" + date_key[:2]

    # Выполнение запроса с аутентификацией
    try:
        response = requests.get(url_event, auth=auth)
        response.raise_for_status()  # Выбрасывает исключение, если статус ответа не 200

        response = response.json()  # Преобразуем ответ в json формат

        data_event = response["event"][:-1] + "."

        event_lst = []

        for i in range(data_event.count(";") + 1):
            index_char = data_event.find(";")

            if index_char != -1:
                event_lst.append(data_event[0 : index_char + 1].strip())
                data_event = data_event[index_char + 1 :]
            elif index_char == -1:
                event_lst.append(data_event.strip())

        return event_lst

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
