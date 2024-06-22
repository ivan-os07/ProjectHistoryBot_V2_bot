import requests

from .server_client import URL
from .event_func import auth

async def test_requests():
    # ps переделать чтобы в рантайме смотрело количество вопросов

    # random_test_number = randint(1, 100)  # Генерирует рандомный номер для подбора теста
    url_date = URL + f"test/{1}"  # Вместо 1 подставить random_test_number

    # Выполнение запроса с аутентификацией
    try:
        response = requests.get(url_date, auth=auth)
        response.raise_for_status()  # Выбрасывает исключение, если статус ответа не 200

        response = response.json()  # Преобразуем ответ в json формат

        return response

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
