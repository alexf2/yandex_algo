from collections import Counter
from dataclasses import dataclass

txt = '''26 февраля 2026 года мир, по преданию, окажется на грани – эту дату связывают
с одним из самых тревожных пророчеств, приписываемых Вольфу Мессингу. Речь идет о документе
из закрытых архивов, который, как утверждается, был обнародован бывшим сотрудником
спецслужб и содержит записи, сделанные медиумом незадолго до его смерти.

Согласно этому тексту, в конце февраля 2026 года человечество окажется в точке максимального
напряжения. День будет отмечен сильным потрясением, после которого планета замрет в
ожидании развития событий. Весь мир, включая Россию, окажется перед жестким выбором между
масштабным конфликтом и попыткой сохранить хрупкий баланс. Ключевую роль, как утверждается,
сыграет конкретный человек "с голубыми глазами", от решения которого будет зависеть
дальнейший ход событий.

В пророчестве фигурирует глобальное противостояние крупных держав – США, Китая и
России. При этом особое внимание уделяется некой скрытой силе, которая не связана с
государствами напрямую, но способна управлять процессами из-за кулис, подталкивая мир
к столкновению ради собственной выгоды. Возможно, речь идет о так называемом "глубинном государстве".
'''

# Делаем Record со значением поля int по умолчанию = 0
# Это нужно, чтобы в value dict хранить object для подсчёта слов, это позволит
# при вызове setdefault использовать одну строчку кода и одно обращение к словарю по ключу.
# Так же, оптимизируем память на эту обёртку через slots.


@dataclass(slots=True)
class Count:
    count: int = 0


def count_words(txt):
    acc = {}
    if not txt or not isinstance(txt, str):
        return acc

    for w in txt.split():
        w = w.lower()
        # тут специально положили в value не int, а oject, чтобы использовать
        # дефолт
        acc.setdefault(w, Count()).count += 1

    return acc


stat = count_words(txt)
print('Total words: ', len(stat), '\n')
for w, c in sorted(stat.items(), key=lambda it: it[1].count, reverse=True):
    print(w, ': ', c.count)

# Это можно переписать через словарь Counter, гораздо короче


@dataclass(slots=True, frozen=True)
class Word:
    w: str


def count_words2(txt):
    if not txt or not isinstance(txt, str):
        return Counter()

    return Counter((Word(w=w.lower()) for w in txt.split()))


stat2 = count_words2(txt)
print('\n\nTotal words: ', len(stat2), '\n')
for w, c in sorted(stat2.items(), key=lambda it: it[1], reverse=True):
    print(w.w, ': ', c)

diff = stat.keys() - set((k.w for k in stat2.keys()))
print('\nDiff: ', diff, len(diff))
