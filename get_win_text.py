"""Генирирует ответ пользователю."""

import random
from dataclasses import dataclass

import settings


@dataclass
class AnswerText:
    """
    Объект ответа бота.

    win_text - дополнительная реакция на самый большой
    и самый маленький выигрыш из предложенных.

    super_prize - дополнительная реакция на самый большой выигрыш из возможных.
    """

    win_text = str
    luck = str | None
    super_prize = str | None


def get_win_text(chances: list, casket: int) -> AnswerText:
    """Генерирует текст выигрыша."""
    answer = AnswerText()
    answer.luck = None
    answer.super_prize = None
    random.shuffle(chances)
    prizes = [
        random.choice(chances),
        random.choice(chances),
        random.choice(chances)
    ]
    # Если призы одинаковые - переигрываем.
    # Если сумма призов больше заданного порога - переигрываем.
    while (
        (prizes[0] == prizes[1] == prizes[2]) or
        sum(prizes) > settings.MAX_SUM_PRIZES
    ):
        prizes = [
            random.choice(chances),
            random.choice(chances),
            random.choice(chances)
        ]

    random.shuffle(prizes)

    bot_game = True
    bot_prize = random.choice(prizes)
    # Если играет человек, запомнить выбранную шкатулку.
    if casket != 0:
        prize = prizes[casket - 1]
        bot_game = False
    else:
        prize = bot_prize

    # Основной текст с выигрышем.
    answer.win_text = settings.WIN_TEXT.format(
        prize=prize, prizes_list=' '.join(map(str, prizes))
    )

    # Дополнительный текст, если приз макисмальный из предложенных.
    if prize == max(prizes):
        if bot_game is True:
            answer.luck = settings.ROBOT_LUCK_TEXT
        else:
            answer.luck = settings.HUMAN_LUCK_TEXT

        # Если приз максимальный из возможных.
        if prize == 100:
            if bot_game is True:
                answer.super_prize = settings.ROBOT_SUPER_PRIZE_TEXT
            else:
                answer.super_prize = settings.HUMAN_SUPER_PRIZE_TEXT

    # Если выбран минимальный из предложенных призов.
    elif prize == min(prizes):
        if bot_game is True:
            answer.luck = settings.ROBOT_DONT_LUCK_TEXT
        else:
            # Если бот тоже выбрал минимальный приз.
            same = ''
            dont_upset = ''
            if bot_prize == prize:
                same = 'тоже '
                dont_upset = 'Так что не расстраивайся.'
            answer.luck = settings.HUMAN_DONT_LUCK_TEXT.format(
                same=same, bot_prize=bot_prize, dont_upset=dont_upset
            )
    return answer
