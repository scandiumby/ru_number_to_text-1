from ..core import get_string_by_number


def test_without_additional():
    number = 100
    assert 'Сто рублей 00 копеек' == get_string_by_number(number)


def test_without_main():
    number = 0.12
    assert 'Ноль рублей 12 копеек' == get_string_by_number(number)


def test_with_main_and_additional():
    number = 122.01
    assert 'Сто двадцать два рубля 01 копейка' == get_string_by_number(number)


def test_with_main_additional_and_currency():
    number = 235.15

    assert 'Двести тридцать пять рублей 15 копеек' == get_string_by_number(
        number=number
    )

def test_with_big_number():
    number = 12345678912.54

    assert ('Двенадцать миллиардов '
            'триста сорок пять миллионов '
            'шестьсот семьдесят восемь тысяч '
            'девятьсот двенадцать рублей 54 копейки' == get_string_by_number(
        number=number
    ))