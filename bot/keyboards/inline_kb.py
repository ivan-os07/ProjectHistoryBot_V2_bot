from random import shuffle, randint

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_main.callback_fact import MainCb, TestCbResponses


# Создание inline клавиатуры, вызываемой при команде start и её заполнение
start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="School", url="https://10ber.uralschool.ru/"),
            InlineKeyboardButton(text="Developer", url="https://vk.com/id495185459"),
        ],
        [
            InlineKeyboardButton(
                text="INFO",
                callback_data="info",
            ),
        ],
    ]
)

# Создание главной inline клавиатуры main и её заполнение
main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Какое сегодня событие?",
                callback_data=MainCb(main_action="event").pack(),
            ),
            InlineKeyboardButton(
                text="Решать тесты",
                callback_data=MainCb(main_action="tests").pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="Давай играть",
                callback_data=MainCb(main_action="game").pack(),
            )
        ],
    ]
)
right_answer_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Продолжить решать тесты",
                callback_data=MainCb(main_action="tests").pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="На главную",
                callback_data="home",
            ),
        ],
    ]
)


# Функция для создания клавиатуры с ответами на вопросы TESTS.
# Принимает key - ответ к тесту и возвращает клавиатуру в одним правильным ответом

async def create_test_ikb(key: int):
    lst = set()
    lst.add(key)
    ikb = InlineKeyboardBuilder()

    while True:
        if len(lst) < 4:
            lst.add(randint(key - 69, key + 169))
        if len(lst) == 4:
            break

    lst = list(lst)  # Преобразуем множество в список для функции ниже
    shuffle(lst)  # Для перемешивания списка
    shuffle(lst)  # Для перемешивания списка

    id_answers = sum(lst) * randint(1, 99)  # Уникальный id вопроса

    for value in lst:
        ikb.button(text=f"{value}",
                   callback_data=TestCbResponses(main_action='answer',
                                                 test_key=value,
                                                 id_kb=id_answers).pack())

    return ikb.as_markup(), id_answers
