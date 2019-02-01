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
        self._assertEqual_with_message_for_conversation(100, 'Сто рублей 00 копеек')

    def test_decimal_part_conversions(self):
        """ Test for decimal part of conversations """
        self._assertEqual_multiply_data(
            (
                (0.12, 'Ноль рублей 12 копеек'),
            )
        )

    def test_integer_and_decimal_part_conversations(self):
        """ Test for decimal and integer part together of conversations """
        self._assertEqual_multiply_data(
            (
                (122.01, 'Сто двадцать два рубля 01 копейка'),
                (235.15, 'Двести тридцать пять рублей 15 копеек'),
                (100500.15, 'Сто тысяч пятьсот рублей 15 копеек'),
                (12345678912.54, 'Двенадцать миллиардов триста сорок пять миллионов шестьсот семьдесят восемь '
                                 'тысяч девятьсот двенадцать рублей 54 копейки')
            )
        )

    def _assertEqual_multiply_data(self, test_input_and_output_dataset: tuple) -> None:
        for number_data, text_data in test_input_and_output_dataset:
            self._assertEqual_with_message_for_conversation(number_data, text_data)

    def _assertEqual_with_message_for_conversation(self, number_data: float, text_data: str) -> None:
        print(f">>> Testing conversation from '{number_data}' to '{text_data}'")
        self.assertEqual(get_string_by_number(number_data), text_data)
