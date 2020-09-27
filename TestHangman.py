import unittest
from Hangman import Hangman


class TestHangmanMaskedWords(unittest.TestCase):
    def setUp(self):
        self.game = Hangman(None, "kotik")

    def test_masked_word(self):
        self.assertEqual(self.game.masked_word, "*****", "Masked word isn't correct")

    def test_right_letter(self):
        self.game.check_letter("t")
        self.assertEqual(self.game.masked_word, "**t**", "Masked word isn't correct")

    def test_wrong_letter(self):
        self.game.check_letter("j")
        self.assertEqual(self.game.masked_word, "*****", "Masked word isn't correct")

    def test_right_word(self):
        self.game.check_word("kotik")
        self.assertEqual(self.game.masked_word, "kotik", "Masked word isn't correct")

    def test_wrong_word(self):
        self.game.check_word("pesik")
        self.assertEqual(self.game.masked_word, "*****", "Masked word isn't correct")
