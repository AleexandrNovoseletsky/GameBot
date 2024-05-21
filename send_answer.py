"""Отправлятель сообщений."""

from time import sleep
from typing import Any

from get_win_text import AnswerText


async def send_answer(chat_id: int, answer: AnswerText, bot: Any) -> None:
    """Отправляет сообщения о выиграшах."""
    await bot.send_message(chat_id=chat_id, text=answer.win_text)
    if answer.luck is not None:
        sleep(1)
        await bot.send_message(chat_id=chat_id, text=answer.luck)
    if answer.super_prize is not None:
        sleep(0.5)
        await bot.send_message(chat_id=chat_id, text=answer.super_prize)
