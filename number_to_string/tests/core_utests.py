import unittest

from number_to_string import get_string_by_number


class GetStringByNumberTests(unittest.TestCase):

    def setUp(self):
        print(f"Set up for [{self.shortDescription()}]")

    def tearDown(self):
        print(f"Tear down for [{self.shortDescription()}]")
        print("")

    def _assertEqual_multiply_data(self, test_input_and_output_dataset: tuple) -> None:
        for number_data, text_data in test_input_and_output_dataset:
            self._assertEqual_with_message_for_conversation(number_data, text_data)

    def _assertEqual_with_message_for_conversation(self, number_data: float, text_data: str) -> None:
        print(f">>> Testing conversation from '{number_data}' to '{text_data}'")
        self.assertEqual(text_data, get_string_by_number(number_data))

    def test_integer_part_less_1000_conversions(self):
        """ Test for integer part of conversations (1-999)"""
        self._assertEqual_multiply_data(
            (
                (1, 'Один рубль 00 копеек'),
                (2, 'Два рубля 00 копеек'),
                (4, 'Четыре рубля 00 копеек'),
                (5, 'Пять рублей 00 копеек'),
                (10, 'Десять рублей 00 копеек'),
                (11, 'Одинадцать рублей 00 копеек'),
                (100, 'Сто рублей 00 копеек'),
                (101, 'Сто один рубль 00 копеек'),
                (999, 'Девятьсот девяносто девять рублей 00 копеек'),
            )
        )

    def test_integer_part_from_1000_to_999999_conversions(self):
        """ Test for integer part of conversations (1000-999999)"""
        self._assertEqual_multiply_data(
            (
                (1000, 'Одна тысяча рублей 00 копеек'),
                (1001, 'Одна тысяча один рубль 00 копеек'),
                (1100, 'Одна тысяча сто рублей 00 копеек'),
                (1101, 'Одна тысяча сто один рубль 00 копеек'),
                (1111, 'Одна тысяча сто одинадцать рублей 00 копеек'),
                (2000, 'Две тысячи рублей 00 копеек'),
                (9000, 'Девять тысяч рублей 00 копеек'),
                (21000, 'Десять тысяча рублей 00 копеек'),
                (101000, 'Сто одна тысяча рублей 00 копеек'),
                (999999, 'Девятьсот девяносто девять тысяч девятьсот девяносто девять рублей 00 копеек'),
            )
        )

    def test_integer_part_from_million_to_999999999_conversions(self):
        """ Test for integer part of conversations (10^6 - 999999999)"""
        self._assertEqual_multiply_data(
            (
                (1000000, 'Один миллион рублей 00 копеек'),
                (1000001, 'Один миллион один рубль 00 копеек'),
                (1000099, 'Один миллион девяносто девять рублей 00 копеек'),
                (1000101, 'Один миллион сто один рубль 00 копеек'),
                (1001000, 'Один миллион одна тысяча рублей 00 копеек'),
                (1001001, 'Один миллион одна тысяча один рубль 00 копеек'),
                (1010101, 'Один миллион десять тысяч сто один рубль 00 копеек'),
                (1010001, 'Один миллион десять тысяч один рубль 00 копеек'),
                (1100001, 'Один миллион сто тысяч один рубль 00 копеек'),
                (10000000, 'Десять миллионов рублей 00 копеек'),
                (10000001, 'Десять миллионов один рубль 00 копеек'),
                (10001000, 'Десять миллионов одна тясяча рублей 00 копеек'),
                (100000000, 'Сто миллионов рублей 00 копеек'),
                (100000001, 'Сто миллионов один рубль 00 копеек'),
                (100001000, 'Сто миллионов одна тысяча рублей 00 копеек'),
                (999999999, 'Девятьсот девяносто девять миллионов девятьсот девяносто девять тысяч девятьсот '
                            'девяносто девять рублей 00 копеек'),
            )
        )

    def test_integer_part_from_billion_to_999999999999_conversions(self):
        """ Test for integer part of conversations (10^9 - 999999999999)"""
        self._assertEqual_multiply_data(
            (
                (1000000000, 'Один миллиард рублей 00 копеек'),
                (1000000001, 'Один миллиард один рубль 00 копеек'),
                (1000001000, 'Один миллиард одна тысяча рублей 00 копеек'),
                (1000001001, 'Один миллиард одна тысяча один рубль 00 копеек'),
                (1001000000, 'Один миллиард один миллион рублей 00 копеек'),
                (1010011100, 'Один миллиард десять миллионов одинадцать тысяч сто рублей 00 копеек'),
                (999999999999, 'Девятьсот девяносто девять миллиардов девятьсот девяносто девять миллионов '
                               'девятьсот девяносто девять тысяч девятьсот девяносто девять рублей 00 копеек'),
            )
        )

    def test_integer_part_trillion_and_more_conversions(self):
        """ Test for integer part of conversations (10^12 and more)"""
        self._assertEqual_multiply_data(
            (
                (1000000000000, 'Один триллион рублей 00 копеек'),
                (999999999999999, 'Девятьсот девяносто девять триллионов девятьсот девяносто девять миллиардов '
                                  'девятьсот девяносто девять миллионов девятьсот девяносто девять тысяч '
                                  'девятьсот девяносто девять рублей 00 копеек'),
            )
        )

    def test_decimal_part_conversions(self):
        """ Test for decimal part of conversations """
        self._assertEqual_multiply_data(
            (
                (0.00, 'Ноль рублей 00 копеек'),
                (0.01, 'Ноль рублей 01 копейка'),
                (0.02, 'Ноль рублей 02 копейки'),
                (0.04, 'Ноль рублей 04 копейки'),
                (0.05, 'Ноль рублей 05 копеек'),
                (0.10, 'Ноль рублей 10 копеек'),
                (0.11, 'Ноль рублей 11 копеек'),
                (0.12, 'Ноль рублей 12 копеек'),
                (0.13, 'Ноль рублей 13 копеек'),
                (0.20, 'Ноль рублей 20 копеек'),
                (0.21, 'Ноль рублей 21 копейка'),
                (0.22, 'Ноль рублей 22 копейки'),
                (0.24, 'Ноль рублей 24 копейки'),
                (0.25, 'Ноль рублей 25 копеек'),
                (0.30, 'Ноль рублей 30 копеек'),
                (0.31, 'Ноль рублей 31 копейка'),
                (0.55, 'Ноль рублей 55 копеек'),
                (0.77, 'Ноль рублей 77 копеек'),
                (0.99, 'Ноль рублей 99 копеек'),
            )
        )

    def test_integer_and_decimal_conversations(self):
        """ Test for decimal and integer part together of conversations """
        self._assertEqual_multiply_data(
            (
                (1.99, 'Один рубль 99 копеек'),
                (122.01, 'Сто двадцать два рубля 01 копейка'),
                (123.99, 'Сто двадцать три рубля 99 копеек'),
                (235.15, 'Двести тридцать пять рублей 15 копеек'),
                (100500.15, 'Сто тысяч пятьсот рублей 15 копеек'),
                (12345678912.54, 'Двенадцать миллиардов триста сорок пять миллионов шестьсот семьдесят восемь '
                                 'тысяч девятьсот двенадцать рублей 54 копейки'),
                (999999999999.99, 'Девятьсот девяносто девять миллиардов девятьсот девяносто девять миллионов '
                                  'девятьсот девяносто девять тысяч девятьсот девяносто девять рублей 99 копеек'),
                (991234567890100.99, 'Девятьсот девяносто один триллион двести тридцать четыре миллиарда '
                                     'пятьсот шестьдесят семь миллионов восемьсот девяносто тысяч '
                                     'сто рублей 99 копеек'),
                (991234567890123.99, 'Девятьсот девяносто один триллион двести тридцать четыре миллиарда '
                                     'пятьсот шестьдесят семь миллионов восемьсот девяносто тысяч '
                                     'сто двадцать три рубля 99 копеек')
            )
        )
