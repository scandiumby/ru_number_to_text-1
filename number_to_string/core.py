from collections import namedtuple


CurrencyInfo = namedtuple('CurrencyInfo', 'base additional')


class NumberToStringHelper:
    """
    Переводит число в строку
    """
    UNITS = [
        '',
        'один',
        'два',
        'три',
        'четыре',
        'пять',
        'шесть',
        'семь',
        'восемь',
        'девять',
        'десять',
        'одинадцать',
        'двенадцать',
        'тринадцать',
        'четырнадцать',
        'пятнадцать',
        'шестнадцать',
        'семнадцать',
        'восемнадцать',
        'девятнадцать',
    ]
    DOZENS = [
        '',
        'десять',
        'двадцать',
        'тридцать',
        'сорок',
        'пятьдесят',
        'шестьдесят',
        'семьдесят',
        'восемьдесят',
        'девяносто',
    ]
    HUNDREDS = [
        '',
        'сто',
        'двести',
        'триста',
        'четыреста',
        'пятьсот',
        'шестьсот',
        'семьсот',
        'восемьсот',
        'девятьсот',
    ]

    def __init__(self, number, currency_main=None, currency_additional=None):
        """

        :param number: int
        :param currency_main:
        :param currency_additional:
        """
        self.number = int(number)
        self.additional = int(round(float(number) - self.number, 3) * 100)
        self.currency_main = currency_main or ('рубль', 'рубля', 'рублей')
        self.currency_additional = (
                currency_additional or
                ('копеек', 'копеек', 'копеек')
        )

    def get_string(self):
        """
        Вовращает число пропусью
        :return: str
        """
        items = self._get_items()

        list_items = []

        value_tuples = (
            ('', '', ''),
            ('тысяча', 'тысячи', 'тысяч'),
            ('миллион', 'миллиона', 'миллионов'),
            ('миллиард', 'миллиарда', 'миллиардов'),
            ('триллион', 'триллиона', 'триллионов'),
            ('квадриллион', 'квадриллиона', 'квадриллионов'),
            ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),
            ('секстиллион', 'секстиллиона', 'секстиллионов'),
            ('септиллион', 'септиллиона', 'септиллионов'),
            ('октиллион', 'октиллиона', 'октиллионов'),
            ('нониллион', 'нониллиона', 'нониллионов'),
            ('дециллион', 'дециллиона', 'дециллионов'),
            ('ундециллион', 'ундециллиона', 'ундециллионов'),
        )
        for i, number in enumerate(items):
            is_thousands = i == 1
            str_number = self._get_str_number(number, is_thousands)
            str_end = self._get_ends(number, value_tuples[i])

            if str_end:
                str_item = ' '.join([str_number, str_end])
            else:
                str_item = str_number

            list_items.append(str_item)

        if items == ['0']:
            list_items = ['ноль']

        base = ' '.join(reversed(list_items))
        pattern = (
            '{base} '
            '{currency_base} '
            '{additional:0>2} '
            '{currency_additional}'
        )
        string = pattern.format(
            base=base,
            currency_base=self._get_main_currency(),
            additional=self.additional,
            currency_additional=self._get_additional_currency()
        )
        return string.capitalize()

    def _get_items(self):
        """
        Разбивает числа по 3 цифры
        Возвращает список
        Сначало еденицы, затем тысячи, затем милионы и так далее
        """
        value = str(self.number)
        items = []
        while len(value) > 3:
            items.append(value[-3:])
            value = value[:-3]
        items.append(value)
        return items

    @staticmethod
    def _get_ends(number, value_tuple=None):
        number = int(number)
        if value_tuple is None:
            value_tuple = ('тысяча', 'тысячи', 'тысяч')

        if (number % 100) > 20:
            number = number % 10
        else:
            number = number % 20
        if number == 1:
            return value_tuple[0]
        elif 2 <= number <= 4:
            return value_tuple[1]
        return value_tuple[2]

    @classmethod
    def _get_str_number(cls, number, is_thousands=False):
        """
        Возвращает сткору числа из трёх чисел

        Пример:
            123 = 'сто двадцать три'
        """
        number = '{:0>3}'.format(number)

        changed_units = cls.UNITS[:]
        if is_thousands:
            changed_units[1] = 'одна'
            changed_units[2] = 'две'

        hundreds = cls.HUNDREDS[int(number[0])]

        dozens = (
            cls.DOZENS[int(number[1])]
            if int(number[1]) != 1
            else changed_units[int(number[1:])]
        )
        units = ''
        if int(number[1]) != 1:
            units = changed_units[int(number[2])]
        list_items = filter(None, [
            hundreds,
            dozens,
            units
        ])
        return ' '.join(list_items)

    def _get_base_currency(self, currency_base, number):
        if self.number % 10 == 1:
            return currency_base[0]
        if 1 < number % 10 < 5:
            return currency_base[1]
        return currency_base[2]

    def _get_main_currency(self):
        return self._get_base_currency(self.currency_main, self.number)

    def _get_additional_currency(self):
        return self._get_base_currency(self.currency_additional, self.number)


def get_string_by_number(number, currency_main=None, currency_additional=None):

    string = NumberToStringHelper(
        number=number,
        currency_main=currency_main,
        currency_additional=currency_additional,
    ).get_string()

    return string
