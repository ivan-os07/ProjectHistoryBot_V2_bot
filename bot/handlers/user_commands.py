import requests

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.inline_kb import start_kb, main_kb

from server_settings import URL, HEADERS_SECRET_KEY

handlers_router = Router()


@handlers_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, <b>{message.from_user.full_name}</b>! 👋\n Я бот, который шарит за историю",
        reply_markup=start_kb,
    )

    await message.answer(
        f"Давай начнём изучать историю 🌏 вместе с <b>Project_History_bot_V2</b>",
        reply_markup=main_kb,
    )

    await add_user(message.from_user.id, message.from_user.full_name)


async def add_user(user_id: int, name: str):
    data = {
        'user_id': user_id,
        'name': name
    }

    response = requests.post(
        f"{URL}user/add/",
        data=data,
        headers={"Authorization": HEADERS_SECRET_KEY}
    )
