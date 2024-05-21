"""Основной модуль."""

import asyncio
import os
import random

from dotenv import load_dotenv
from telebot import types
from telebot.async_telebot import AsyncTeleBot

from generate_prizes_list import get_chances
from get_win_text import get_win_text
from send_answer import send_answer
from settings import HELLO

load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
GameBot = AsyncTeleBot(token=token, parse_mode=None)
chances = get_chances()
random.shuffle(chances)


def main() -> None:
    """Фкнкция запуска."""

    @GameBot.message_handler(func=lambda m: True, content_types='text')
    async def listener(message: types.Message) -> None:
        random.shuffle(chances)
        text_message = message.text.lower().replace(' ', '')
        match text_message:
            case 'играю' | 'игра' | '$':
                await GameBot.send_message(message.chat.id, text=HELLO)
                random.shuffle(chances)
                return

            case (
                'шкатулка0' | 'шкатулка1' | 'шкатулка2' |
                'шкатулка3' | 'ш0' | 'ш1' | 'ш2' | 'ш3'
            ):
                random.shuffle(chances)
                casket = int(text_message[-1])
                answer = get_win_text(chances=chances, casket=casket)
                await send_answer(
                    chat_id=message.chat.id, answer=answer, bot=GameBot)
                random.shuffle(chances)

    asyncio.run(GameBot.infinity_polling())


if __name__ == '__main__':
    main()
