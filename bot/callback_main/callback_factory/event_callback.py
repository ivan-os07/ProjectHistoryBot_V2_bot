import datetime

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery

from callback_main.callback_fact import MainCb

from server_func.event_func import event_request


event_cb_router = Router()


# Функция для обработки кнопки Какое сегодня событие?
@event_cb_router.callback_query(MainCb.filter(F.main_action == "event"))
async def event(callback: CallbackQuery):
    today = str(datetime.date.today())  # Сегодняшний день
    key = today[5:]

    await callback.answer(cache_time=10)  # Для анти спама
    await callback.message.answer(text=f"Событие на сегодня (<b>{today}</b>):")

    event_data = await event_request("01-01")  # Здесь будет key

    for i in event_data:
        await callback.message.answer(text=f"<b>{i}</b>")
