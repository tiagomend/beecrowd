from unittest import TestCase, main
from unittest.mock import patch

from main import simple_product

class TestSimpleProduct(TestCase):
    @patch('builtins.input', side_effect=['3', '9'])
    def test_first(self, _):
        self.assertEqual(simple_product(), 'PROD = 27')

    @patch('builtins.input', side_effect=['-30', '10'])
    def test_second(self, _):
        self.assertEqual(simple_product(), 'PROD = -300')

    @patch('builtins.input', side_effect=['0', '9'])
    def test_third(self, _):
        self.assertEqual(simple_product(), 'PROD = 0')

if __name__ == '__main__':
    main()
