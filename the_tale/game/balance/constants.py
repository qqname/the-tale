# coding: utf-8

import math

TIME_TO_LVL_DELTA = float(5) # разница во времени получения двух соседних уровней

INITIAL_HP = int(300) # начальное здоровье героя

HP_PER_LVL = int(30) # бонус к здоровью на уровень

MOB_HP_MULTIPLIER = float(0.25) # какой процент здоровье среднего моба составляет от здоровья героя

TURN_DELTA = int(10)  # в секундах - задержка одного хода

TURNS_IN_HOUR = float(60.0 * 60 / TURN_DELTA) # количество ходов в 1 часе

POWER_PER_LVL = int(1) # значение "чистой" силы героя (т.е. без артефактов)

EQUIP_SLOTS_NUMBER = int(12) # количество слотов экипировки

ARTIFACTS_PER_LVL = int(4) # количество новых артефактов, на уровень героя

EXP_PER_MOB = float(1) # опыт, получаемый за убийство одного моба

BATTLE_LENGTH = int(16) # ходов - средняя длительность одного боя (количество действий в бой)
INTERVAL_BETWEEN_BATTLES = int(5) # ходов - время, между двумя битвами

BATTLES_BEFORE_HEAL = int(10) # количество боёв в непрерывной цепочке битв

HEAL_TIME_FRACTION = float(0.2) # доля времени от цепочки битв, которую занимает полный отхил героя

HEALTH_IN_SETTLEMENT_TO_START_HEAL_FRACTION = float(0.33) # если у героя здоровья меньше, чем указанная доля и он в городе, то он будет лечиться
HEALTH_IN_MOVE_TO_START_HEAL_FRACTION = (2 *float(1)) / BATTLES_BEFORE_HEAL # если у героя здоровья меньше, чем указанная доля и он в походе, то он будет лечиться


GET_LOOT_PROBABILITY = float(0.33) # вероятность получить лут после боя, если не получен артефакт

# вероятности получить разный тип лута

NORMAL_LOOT_PROBABILITY = float(0.99)
RARE_LOOT_PROBABILITY = float(0.0099)
EPIC_LOOT_PROBABILITY = 1 - NORMAL_LOOT_PROBABILITY - RARE_LOOT_PROBABILITY

#стоимость разного лута на единицу уровня
NORMAL_LOOT_COST = float(1.5)
RARE_LOOT_COST = float(25)
EPIC_LOOT_COST = float(250)

MAX_BAG_SIZE = int(12) # максимальный размер рюкзака героя
BAG_SIZE_TO_SELL_LOOT_FRACTION = float(0.33) # процент заполненности рюкзака, после которого герой начнёт продавать вещи

# относительные размеры различных трат

INSTANT_HEAL_PRICE_FRACTION = float(0.3) # моментальное лечение
BUY_ARTIFACT_PRICE_FRACTION = float(2.0) # покупка нового артефакта
SHARPENING_ARTIFACT_PRICE_FRACTION = float(0.7) # "заточка" экипированного артефакта
USELESS_PRICE_FRACTION = float(0.2) # безполезные траты
IMPACT_PRICE_FRACTION = float(1.5) # изменение (+/-) влияния персонажей

SELL_ARTIFACT_PRICE_FRACTION = float(0.5) # часть цены, за которую артефакты продаются

PRICE_DELTA = float(0.2) # дельта на цену PRICE * (1 + random.uniform(-0.2, 0.2))

POWER_TO_LVL = float(EQUIP_SLOTS_NUMBER) # бонус к ожидаемой силе на уровнеь героя

# Разброс силы артефактов делаем от -ItemPowerDelta до +ItemPowerDelta.
# за базу берём количество слотов, т.е., теоретически, может не быть предметов с повторяющейся силой
# что бы не вводить дизбаланса, надо на маленьких уровнях уменьшать делту, что бу разница уровня предмета и дельты была неменьше единицы
ARTIFACT_POWER_DELTA = int(EQUIP_SLOTS_NUMBER / 2) # дельта, на которую может изменяться сила артифакта

# ходов - длинна непрерывной цепочки боёв до остановки на лечение
BATTLES_LINE_LENGTH = int(BATTLES_BEFORE_HEAL * (BATTLE_LENGTH + INTERVAL_BETWEEN_BATTLES ) - INTERVAL_BETWEEN_BATTLES)

HEAL_LENGTH = int(math.floor(BATTLES_LINE_LENGTH * HEAL_TIME_FRACTION)) # ходов - длительность лечения героя

ACTIONS_CYCLE_LENGTH = int(BATTLES_LINE_LENGTH + HEAL_LENGTH) # ходов - длинна одного "игрового цикла" - цепочка боёв + хил
BATTLES_PER_HOUR = float(TURNS_IN_HOUR) / ACTIONS_CYCLE_LENGTH * BATTLES_BEFORE_HEAL # количество битв в час

DAMAGE_TO_HERO_PER_HIT_FRACTION = float(1.0 / (BATTLES_BEFORE_HEAL * BATTLE_LENGTH / 2)) # доля урона, наносимого герою за удар
DAMAGE_TO_MOB_PER_HIT_FRACTION = float(1.0 / (BATTLE_LENGTH / 2)) # доля урона, наносимого мобу за удар

EXP_PER_HOUR = float(BATTLES_PER_HOUR * EXP_PER_MOB)  # опыт в час ;

# таким образом, напрашиваются следующие параметры мобов:
# - здоровье, в долях от среднемобского - чем больше его, тем  дольше моб живёт
#  - инициатива, в долях относительно геройской - чем больше, тем чаще моб ходит
#  - урон, в долях от среднемобского - чем больше, тем больнее бьёт
#  - разброс урона, в долях от среднего - декоративный параметр, т.к. в итоге будет средний урон наноситься
# так как все параметры измеряются в долях, то сложность моба можно высчитать как hp * initiative * damage = 1 для среднего моба
# моб со всеми парамтрами, увеличеными на 10% будет иметь сложность 1.1^3 ~ 1.33
# соответственно, вводня для каждого параметра шаг в 0.1 и скалируя от 0.5 до 1.5, получим 11^3 вариантов параметров (и, соответственно поведения)
# сложность мобов в этом случае будет изменяться от 0.5^3 до 1.5^3 ~ (0.125, 3.375)
#
# возникает проблема обеспечения равномерности прокачки героев на разных территориях - для полностью честных условий необходимо обеспечить одинаковую сложность мобов,
# альтернативный вариант - изменять количесво опыта, даваемого за моба, в зависимости от его сложности, этот вариант кажется как более логичным с точки зрения игрока, так и простым в реализации, на нём и остановимся
#
# расчёт прочего лута и золота: добыча/трата

# считаем, что если герой не выбил артефакт, то у него есть вероятность выбить лут
# лут делим на обычный, редкий и очень редкий
# лут является основным источником дохода, вырученное за его продажу золото является функцией от уровня и редкости - т.е. есть три фунции от уровня
# лут, как и мобы, организован в список, отсортированый по уровню, на котором он становится доступным, это позволит открывать игрокам новый контент, а так же сделать разброс цен



# разные левые "неприкаянные" константы
