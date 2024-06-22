from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_lst) -> None:
        self.admin_lst = admin_lst

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_lst
