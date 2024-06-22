import requests
import os

from dotenv import load_dotenv, find_dotenv

# URL API-endpoint
URL = "http://127.0.0.1:8000/api/v1/"


# Учетные данные для аутентификации
load_dotenv(find_dotenv())
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


# Создаем объект аутентификации
auth = requests.auth.HTTPBasicAuth(username, password)
