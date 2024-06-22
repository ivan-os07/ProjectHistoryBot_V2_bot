from aiogram.filters.callback_data import CallbackData


class MainCb(CallbackData, prefix="pre"):
    main_action: str


class TestCbResponses(CallbackData, prefix="pre"):
    main_action: str
    test_key: int
    id_kb: int
