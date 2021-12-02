from unittest import TestCase
from src.main import Game

class TestCheckWin(TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_empty_board_is_false(self):
        test_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.game.board = test_board
        self.assertFalse(self.game.check_win('x'))

    def test_first_column_is_true(self):
        test_board = [['x', '_', '_'], ['x', '_', '_'], ['x', '_', '_']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_second_column_is_true(self):
        test_board = [['_', 'x', '_'], ['_', 'x', '_'], ['_', 'x', '_']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_third_column_is_true(self):
        test_board = [['_', '_', 'x'], ['_', '_', 'x'], ['_', '_', 'x']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_first_row_is_true(self):
        test_board = [['x', 'x', 'x'], ['_', '_', '_'], ['_', '_', '_']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_second_row_is_true(self):
        test_board = [['_', '_', '_'], ['x', 'x', 'x'], ['_', '_', '_']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_third_row_is_true(self):
        test_board = [['_', '_', '_'], ['_', '_', '_'], ['x', 'x', 'x']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_diag1_is_true(self):
        test_board = [['x', '_', '_'], ['_', 'x', '_'], ['_', '_', 'x']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))

    def test_diag2_is_true(self):
        test_board = [['_', '_', 'x'], ['_', 'x', '_'], ['x', '_', '_']]
        self.game.board = test_board
        self.assertTrue(self.game.check_win('x'))