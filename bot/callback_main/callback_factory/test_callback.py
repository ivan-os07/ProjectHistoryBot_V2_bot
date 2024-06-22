from random import randint

import requests

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackQuery


from keyboards.inline_kb import create_test_ikb, right_answer_kb
from callback_main.callback_fact import MainCb, TestCbResponses

from server_func.test_func import test_requests


test_cb_router = Router()

id_answers: int
key_answer: int


# функция для обработки кнопки решать тесты
@test_cb_router.callback_query(MainCb.filter(F.main_action == "tests"))
async def main_tests(callback: CallbackQuery, callback_data: MainCb):
    global id_answers  # Переменная для проверки соответствующего вопроса
    global key_answer  # Сам ответ на вопрос

    res = await test_requests()

    key_answer = res["key"]  # Ответ на вопрос

    response_from_ikb = await create_test_ikb(key_answer)

    kb = response_from_ikb[0]  # Клавиатура с вариантами ответов
    id_answers = response_from_ikb[1]  # Уникальный id для вопроса

    await callback.answer(cache_time=1)  # Для анти спама

    await callback.message.answer(text=res["question"], reply_markup=kb)


# функция для обработки тестов
@test_cb_router.callback_query(TestCbResponses.filter(F.main_action == "answer"))
async def tests(callback: CallbackQuery, callback_data: TestCbResponses):
    # await callback.answer(cache_time=10)  # Для анти спама

    if callback_data.id_kb == id_answers:  # Сравниваем уникальный id
        if callback_data.test_key == key_answer:  # Проверяем правильный ответ
            await callback.message.answer(
                text="Молодец! Правильно", reply_markup=right_answer_kb
            )
            await callback.answer()
        else:
            await callback.answer(text="Неверно, попробуй другой вариант")
            await callback.answer()
    else:
        await callback.answer(text="Этот ответ не на тот вопрос!", show_alert=True)
