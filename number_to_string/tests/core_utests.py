import unittest

from number_to_string import get_string_by_number


class GetStringByNumberTests(unittest.TestCase):

    def setUp(self):
        print(f"Set up for [{self.shortDescription()}]")

    def tearDown(self):
        print(f"Tear down for [{self.shortDescription()}]")
        print("")

    def test_integer_part_conversions(self):
        """ Test for integer part of conversations """
        self._assertEqual_with_message_for_conversation('Сто рублей 00 копеек', 100)

    def test_decimal_part_conversions(self):
        """ Test for decimal part of conversations """
        self._assertEqual_with_message_for_conversation('Ноль рублей 12 копеек', 0.12)

    def test_integer_and_decimal_part_conversations(self):
        """ Test for decimal and integer part together of conversations """
        test_input_and_output_dataset = (
            ('Сто двадцать два рубля 01 копейка', 122.01),
            ('Двести тридцать пять рублей 15 копеек', 235.15),
            ('Сто тысяч пятьсот рублей 15 копеек', 100500.15),
            ('Двенадцать миллиардов триста сорок пять миллионов шестьсот семьдесят восемь тысяч девятьсот двенадцать '
             'рублей 54 копейки', 12345678912.54)
        )
        for text_data, number_data in test_input_and_output_dataset:
            self._assertEqual_with_message_for_conversation(text_data, number_data)

    def _assertEqual_with_message_for_conversation(self, text_data: str, number_data: float) -> None:
        print(f">>> Testing conversation from {number_data} to {text_data}")
        self.assertEqual(text_data, get_string_by_number(number_data))
