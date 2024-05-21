"""Генерирует список призов."""

import random

from settings import MAX_PRIZE


def get_chances():
    """
    Генерирует список призов.

    prizes_list((X, Y),): где X - это размер приза,
    а Y - это шанс его выпадедения.
    Представьте что в корзину кладутся лотерейные билеты,
    X - это сумма выигрыша на билете,
    а Y - это сколько такиз билетов мы положим в корзину.
    """
    prizes_chances = (
        (200, 20), (250, 15), (300, 10), (350, 6), (500, 3), (MAX_PRIZE, 1)
    )

    prizes_list = []
    for prize, chance in prizes_chances:
        prizes_list.extend([prize for _ in range(chance)])

    random.shuffle(prizes_list)
    return prizes_list
