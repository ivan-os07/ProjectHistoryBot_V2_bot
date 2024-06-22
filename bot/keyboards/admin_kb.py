from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from server_settings import URL_ADMIN


admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text='Получить справку о пользователях',
                                 callback_data='test'),
        ],
        [
            InlineKeyboardButton(text='Добавить тест',
                                 callback_data='addTest')
        ],
        [
            InlineKeyboardButton(text='Сайт админа',
                                 url=URL_ADMIN)
        ],
    ]
)

add_test_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить тест',
                                 callback_data='addTestFinal'),
            InlineKeyboardButton(text='Не добавлять тест',
                                 callback_data='notAddTest')
        ]
    ]
)