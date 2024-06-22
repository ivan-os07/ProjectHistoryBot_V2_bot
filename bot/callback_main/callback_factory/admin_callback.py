import requests

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message

from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.admin_kb import add_test_kb
from server_settings import URL, HEADERS_SECRET_KEY

admin_cb_router = Router()
user_data = {}


class AddTest(StatesGroup):
    test_step = State()
    answer_step = State()


@admin_cb_router.callback_query(StateFilter(None), F.data == "addTest")
async def add_test(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Введите текст теста")
    await state.set_state(AddTest.test_step)
    await callback.answer()


@admin_cb_router.message(AddTest.test_step)
async def add_answer(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    await message.answer(text="Введите правильный ответ к этому тесту (число)")
    await state.set_state(AddTest.answer_step)


@admin_cb_router.message(AddTest.answer_step)
async def add_answer(message: Message, state: FSMContext):
    try:
        int(message.text)
        global user_data
        await state.update_data(key=int(message.text))

        user_data = await state.get_data()
        await state.clear()

        await message.answer(
            text=f'Ваш вопрос:\n{user_data["question"]}\nс ответом: {user_data["key"]}',
            reply_markup=add_test_kb,
        )
    except ValueError:
        await message.answer(text="Нужно ввести число")


@admin_cb_router.callback_query(F.data == "addTestFinal")
async def add_test(callback: CallbackQuery):
    url_test = URL + "add_test/"
    res = requests.post(
        url_test,
        headers={"Authorization": HEADERS_SECRET_KEY},
        data={"question": user_data["question"], "key": user_data["key"]},
    )

    if res.status_code == 201:
        await callback.message.answer(text="Тест добавился")
    else:
        await callback.message.answer(text="Возникла ошибка")
