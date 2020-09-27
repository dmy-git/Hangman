import random


def read_words(filename):
    file = open(filename)
    words = file.readlines()
    return words


class Hangman:
    standart_filename = "words.txt"
    attempts = 5
    mistakes = 0

    def __init__(self, filename=standart_filename, word=None):
        if filename is not None:
            self.words = read_words(filename)

        self.word = self.words[random.randrange(0, len(self.words), 1)]\
            .strip().lower()
        self.count_letters = len(self.word)
        self.masked_word = '*' * self.count_letters
        print(self.masked_word)

    def play(self):
        while self.mistakes < self.attempts and not self.is_word_opened():
            letter = input("Guess a letter: ").lower()
            if len(letter) == 1:
                self.check_letter(letter)
            else:
                self.check_word(letter)
        if self.mistakes == self.attempts:
            print("You lost!")

    def check_word(self, word):
        if word == self.word:
            print("You won!")
            self.masked_word = self.word
        else:
            self.mistakes += 1
            print("Missed, mistake " + str(self.mistakes)
                  + " out of " + str(self.attempts) + ".")
        print("The word: " + self.masked_word)

    def check_letter(self, letter):
        if letter in self.word:
            print("Hit!")
            index = self.word.find(letter)
            while index != -1:
                self.masked_word = self.masked_word[:index] \
                                   + letter + self.masked_word[index + 1:]
                index = self.word.find(letter, index + 1)
            if self.is_word_opened():
                print("You won!")
        else:
            self.mistakes += 1
            print("Missed, mistake " + str(self.mistakes)
                  + " out of " + str(self.attempts) + ".")
        print("The word: " + self.masked_word)

    def is_word_opened(self):
        return self.masked_word == self.word


game = Hangman()
game.play()
