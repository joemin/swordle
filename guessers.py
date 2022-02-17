import re

from constants import CORRECT
from constants import MISPLACED
from constants import WRONG
import constraints

'''
The naive guesser will only guess from the solutions.
'''
class NaiveGuesser:
    def __init__(self, scored_words):
        self.constraints = constraints.Constraints()
        # scored_words is the sorted list of word/score tuples for solutions
        self.scored_words = scored_words
        self.guesses = []

    def next_guess(self):
        def has_repeat_char(word):
            return len(set(word)) != len(word)
        next_guess = None
        for s_w in self.scored_words:
            w = s_w[0]
            if (self.constraints.meets_constraints(w)):
                # Do not to repeat for the first two guesses
                if has_repeat_char(w) and len(self.guesses) < 2:
                    # But, just in case, save this for later
                    if next_guess == None:
                        next_guess = w
                    continue
                self.guesses.append(w)
                return w
        self.guesses.append(next_guess)
        return next_guess

    def update_constraints(self, guess, checked_row):
        new_global_constraints = []

        constraints_by_position = ['^', '^', '^', '^', '^']
        seen = []
        for i in range(len(checked_row)):
            state = checked_row[i]
            if state == MISPLACED:
                constraints_by_position[i] += guess[i]
                new_global_constraints.append(guess[i])
            elif (state == WRONG):
                if (guess[i] not in seen):
                    for j in range(len(constraints_by_position)):
                        constraints_by_position[j] += guess[i]
                else:
                    constraints_by_position[i] += guess[i]
            seen.append(guess[i])

        # Do that again for CORRECT letters to override any regex
        # derived from MISPLACED letters
        for i in range(len(checked_row)):
            state = checked_row[i]
            if state == CORRECT:
                constraints_by_position[i] = guess[i]
                new_global_constraints.append(guess[i])

        # Now generate a regex string like: '^[^ba][e][^ba][^ba][^ba]$'
        # for the positional constraints
        new_positional_constraint = f'^[{"][".join(constraints_by_position)}]$'
        self.constraints.update_positional_constraints(
            new_positional_constraint
        )
        self.constraints.update_global_constraints(new_global_constraints)
