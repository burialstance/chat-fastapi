from enum import Enum


class GendersEnum(str, Enum):
    MALE = 'мужской'
    FEMALE = 'женский'


class MessengersEnum(str, Enum):
    VKONTAKTE = 'vkontakte'
    TELEGRAM = 'telegram'