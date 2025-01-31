from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON

router = Router()


# Этот хендлер будет реагировать на любые сообщения пользователя, 
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(text=LEXICON['error_message'])




