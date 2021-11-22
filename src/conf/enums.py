from enum import Enum


class GendersEnum(str, Enum):
    MALE = 'мужской'
    FEMALE = 'женский'


class MessengersEnum(str, Enum):
    VKONTAKTE = 'vkontakte'
    TELEGRAM = 'telegram'


class CountriesEnum(str, Enum):
    RUSSIA = 'Россия'
    UKRAINE = 'Украина'
    BELARUS = 'Беларусь'
    KAZAKHSTAN = 'Казахстан'
    UZBEKISTAN = 'Узбекистан'
    TAJIKISTAN = 'Таджикистан'
    TURKMENISTAN = 'Туркменистан'
    AZERBAIJAN = 'Азербайджан'
    ARMENIA = 'Армения'
    MOLDOVA = 'Молдова'
