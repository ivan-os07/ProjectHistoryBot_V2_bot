from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from handlers.admin_filter import IsAdmin
from keyboards.admin_kb import admin_kb

admin_lst = [1703186969]

admin_router = Router()
admin_router.message.filter(IsAdmin(admin_lst))  # Подключаем фильтр на админа


@admin_router.message(Command('admin'))
async def admin_start_handler(message: Message) -> None:
    await message.answer(text='Вас приветствует меню админа', reply_markup=admin_kb)



