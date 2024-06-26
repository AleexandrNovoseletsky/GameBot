"""
Настройки.

Чтобы отредактировать призы, редактируй файл generate_prizes_list
"""

# Максимально возможный приз.
MAX_PRIZE: int = 1000

# Лимит максимальной суммы шкатулок.
# Если сумма трёх шкатулок привысит этот лимит, призы будут обновлены.
MAX_SUM_PRIZES: int = 1700

# Шаблон основного сообщения о выигрыше.
WIN_TEXT: str = (
    'Ты выиграл {prize} рублей.\nПризы были такими {prizes_list}'
)

# Максимальный выигрыш из предложенных трёх шкатулок.
HUMAN_LUCK_TEXT: str = 'Ну у тебя и чуйка!'
ROBOT_LUCK_TEXT: str = 'Ну у меня и чуйка! Лучше чем у тебя)'

# Максимальный выигрыш из возможных.
HUMAN_SUPER_PRIZE_TEXT: str = (
    'Это СУПЕРПРИЗ!!!\n'
    'Теперь ты можешь начать копить на А-А-ААА-ААААА-ВТОМОБИЛЬ!'
)
ROBOT_SUPER_PRIZE_TEXT: str = (
    'Это суперприз!\n'
    'Теперь ты можешь начать копить на А-А-ААА-ААААА-ВТОМОБИЛЬ!\n'
    'Покатаешь потом меня? Это же я выиграл!'
)

# Минимальный выигрыш из предложенных.
HUMAN_DONT_LUCK_TEXT: str = (
    'Ты выбрал самый маленький приз. Я рад! Если бы '
    'ты выбрал шкатулку 0, то {same}выиграл бы {bot_prize}р.\n'
    '{dont_upset}'
)
ROBOT_DONT_LUCK_TEXT: str = (
    'Я специально выбрал самый маленький приз, '
    'чтобы тебе было приятно! '
    'Я плохо понимаю что приятно человекам, не осуждай меня.'
)

HELLO: str = (
    'У Вас есть право на три шкатулки.\n'
    'В каждой из них лежат случайные призы, выбирай одну.\n'
    'Напиши слово шкатулка и цифру от 1 до 3, например - "Шкатулка 1".\n'
    'Если хочешь чтобы я выбрал за тебя, напиши - "Шкатулка 0".'
)
