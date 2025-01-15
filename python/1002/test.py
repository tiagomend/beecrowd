from unittest import TestCase, main
from unittest.mock import patch

from main import calculate_circle_area


class TestCircleArea(TestCase):
    @patch('builtins.input', side_effect=['2.00'])
    def test_first(self, _):
        self.assertEqual(calculate_circle_area(), 'A=12.5664')

    @patch('builtins.input', side_effect=['100.64'])
    def test_second(self, _):
        self.assertEqual(calculate_circle_area(), 'A=31819.3103')

    @patch('builtins.input', side_effect=['150.00'])
    def test_third(self, _):
        self.assertEqual(calculate_circle_area(), 'A=70685.7750')

if __name__ == '__main__':
    main()
