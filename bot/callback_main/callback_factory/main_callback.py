from aiogram.filters.callback_data import CallbackQuery
from aiogram import Router, F

from keyboards.inline_kb import main_kb

main_callback_router = Router()


# функция для обработки кнопки INFO
@main_callback_router.callback_query(F.data == "info")
async def info(callback: CallbackQuery):
    await callback.answer(cache_time=10)  # Для анти спама
    await callback.message.answer(
        text=f"<i>Если у вас возникли вопросы и предложения, обратитесь к разработчику</i>✍️ @iChizh007"
    )


# функция для возврата на главное меню
@main_callback_router.callback_query(F.data == 'home')
async def home_page(callback: CallbackQuery):
    await callback.answer(cache_time=10)
    await callback.message.answer(
        f"Давай начнём изучать историю 🌏 вместе с <b>Project_History_bot_V2</b>",
        reply_markup=main_kb,
    )
