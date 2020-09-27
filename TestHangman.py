import unittest
import sys
import io
from Hangman import Hangman


class TestHangmanImport(unittest.TestCase):
    def test_import_std_file(self):
        std_file = open("words.txt")
        std_words = std_file.readlines()
        std_file.close()
        self.game = Hangman()
        self.assertEqual(len(self.game.words), len(std_words), "Imported word isn't correct")

    def test_imported_word(self):
        self.game = Hangman("test.txt")
        self.assertEqual(self.game.word, "test", "Imported word isn't correct")


class TestHangmanGameplay(unittest.TestCase):
    def setUp(self):
        self.game = Hangman(None, "kotik")
        self.saved_stdout = sys.stdout

    def test_is_word_opened(self):
        self.game.check_word("kotik")
        self.assertTrue(self.game.is_word_opened())

    def test_the_word_guessed(self):
        try:
            out = io.StringIO()
            sys.stdout = out
            self.game.check_word("kotik")
            output = out.getvalue().strip()
            self.assertTrue(output.endswith("The word: kotik"))
        finally:
            sys.stdout = self.saved_stdout

    def test_the_word_missed(self):
        try:
            out = io.StringIO()
            sys.stdout = out
            self.game.check_word("pesik")
            output = out.getvalue().strip()
            self.assertTrue(output.endswith("The word: *****"))
        finally:
            sys.stdout = self.saved_stdout

    def test_the_letter_guessed(self):
        try:
            out = io.StringIO()
            sys.stdout = out
            self.game.check_letter("k")
            output = out.getvalue().strip()
            self.assertTrue(output.endswith("The word: k***k"))
        finally:
            sys.stdout = self.saved_stdout

    def test_the_letter_missed(self):
        try:
            out = io.StringIO()
            sys.stdout = out
            self.game.check_letter("p")
            output = out.getvalue().strip()
            self.assertTrue(output.endswith("The word: *****"))
        finally:
            sys.stdout = self.saved_stdout


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
