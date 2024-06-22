from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery

from callback_main.callback_fact import MainCb

game_cb_router = Router()


# функция для обработки кнопки давай играть
@game_cb_router.callback_query(MainCb.filter(F.main_action == "game"))
async def game(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    await callback.message.answer(text=f"Здесь будет игра")
