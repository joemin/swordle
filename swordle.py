import random

from constants import CORRECT
from constants import MISPLACED
from constants import WRONG
from word_lists import solutions

'''
This class is the verifier for swordle.
Its main purpose is to take guesses and check it against its solution.
'''
class Swordle:
    def __init__(self, solution='', word_list=solutions):
        self.solution = solution
        if not self.solution:
            self.solution = solutions[random.randint(0, len(solutions))]

    def is_solution(self, guess):
        return guess == self.solution

    def check_guess(self, guess):
        checked_row = ['', '', '', '', '']
        unique_letters = set(guess)
        for letter in unique_letters:
            indices_of_letter_in_guess = []
            for i in range(len(guess)):
                if guess[i] == letter:
                    indices_of_letter_in_guess.append(i)
            indices_of_letter_in_solution = []
            for i in range(len(self.solution)):
                if (self.solution[i] == letter):
                    indices_of_letter_in_solution.append(i)

            for i in indices_of_letter_in_guess:
                if len(indices_of_letter_in_solution):
                    # CORRECT first
                    correct_indices = list(
                        set(indices_of_letter_in_guess) &
                        set(indices_of_letter_in_solution)
                    )
                    for correct_index in correct_indices:
                        checked_row[correct_index] = CORRECT
                        indices_of_letter_in_guess.remove(correct_index)
                        indices_of_letter_in_solution.remove(correct_index)
                else:
                    checked_row[i] = WRONG
            # If, after removing CORRECTs, there are still instances of
            # letter, deal with them now
            for i in indices_of_letter_in_guess:
                if len(indices_of_letter_in_solution):
                    indices_of_letter_in_solution.pop(0)
                    checked_row[i] = MISPLACED
                else:
                    checked_row[i] = WRONG
        return checked_row
