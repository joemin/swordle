import re

class Constraints:
    def __init__(self):
        # Positional constraints is a list of regex expressions
        # that each will describe a word that is exactly 5 letters long
        self.positional_constraints = ['^[a-z][a-z][a-z][a-z][a-z]$']
        # Global constraints is a list of letters that must be present
        # _somewhere_ in the word
        self.global_constraints = []

    def meets_constraints(self, word):
        # Make sure positional regexes are fully met
        for positional_constraint in self.positional_constraints:
            meets_positional_constraint = bool(re.fullmatch(
                positional_constraint, word
            ))
            if not meets_positional_constraint:
                return False
        # And also global constraints are all present
        word_letters = list(word)
        for letter in self.global_constraints:
            if letter not in word_letters:
                return False
            letter_index = word_letters.index(letter)
            meets_global_constraint = letter_index >= 0
            if not meets_global_constraint:
                return False
            del word_letters[letter_index]
        return True

    def update_positional_constraints(self, new_positional_constraint):
        self.positional_constraints.append(new_positional_constraint)

    def update_global_constraints(self, new_global_constraints):
        self.global_constraints = new_global_constraints
