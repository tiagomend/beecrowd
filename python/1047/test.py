from unittest import TestCase, main
from unittest.mock import patch

from main import *

class TestGameTimeInMinutes(TestCase):
    def test_hours_to_minutes(self):
        self.assertEqual(420, hours_to_minutes(7))
    
    def test_minutes_to_hours(self):
        self.assertEqual((2, 2), minutes_to_hours(122))

    def test_calculation_duration(self):
        self.assertEqual(238, calculate_duration(1322, 120))

    @patch('builtins.input', side_effect=['7 8 9 10'])
    def test_split_input(self, _):
        self.assertEqual([7, 8, 9, 10], split_input())

    @patch('builtins.input', side_effect=['7 8 9 10'])
    def test_game_time_in_minutes_first(self, _):
        expect = 'O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)'
        self.assertEqual(expect, game_time_in_minutes())

    @patch('builtins.input', side_effect=['7 7 7 7'])
    def test_game_time_in_minutes_second(self, _):
        expect = 'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)'
        self.assertEqual(expect, game_time_in_minutes())
    
    @patch('builtins.input', side_effect=['7 10 8 9'])
    def test_game_time_in_minutes_third(self, _):
        expect = 'O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)'
        self.assertEqual(expect, game_time_in_minutes())

    @patch('builtins.input', side_effect=['22 10 3 12'])
    def test_game_time_in_minutes_third(self, _):
        expect = 'O JOGO DUROU 5 HORA(S) E 2 MINUTO(S)'
        self.assertEqual(expect, game_time_in_minutes())

if __name__ == '__main__':
    main()
