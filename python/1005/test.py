from unittest import TestCase, main
from unittest.mock import patch

from main import *

class TestAverageOne(TestCase):
    @patch('builtins.input', side_effect=[5.0, 7.1])
    def test_first(self, _):
        self.assertEqual('MEDIA = 6.43182', average_one())

    @patch('builtins.input', side_effect=[0.0, 7.1])
    def test_two(self, _):
        self.assertEqual('MEDIA = 4.84091', average_one())

    @patch('builtins.input', side_effect=[10.0, 10.0])
    def test_three(self, _):
        self.assertEqual('MEDIA = 10.00000', average_one())

if __name__ == '__main__':
    main()
