import json

from train import train_by_position
from word_lists import solutions
import guessers, swordle


total_num_guesses = 0
longer_than_6 = []
stats_map = {}

list_length = len(solutions)
scored_words = train_by_position(False, False)

for i in range(list_length):
    guesser = guessers.NaiveGuesser(scored_words)
    word = solutions[i]
    current_game = swordle.Swordle(word)

    print(i, word)

    solution_found = False
    guesses = 0
    while not solution_found and guesses <= 10:
        guesses += 1
        next_guess = guesser.next_guess()
        if current_game.is_solution(next_guess):
            solution_found = True
        guesser.update_constraints(next_guess, current_game.check_guess(next_guess))

    stats_map[guesses] = stats_map.get(guesses, 0)+1
    if guesses > 6:
        longer_than_6.append((word, guesses, guesser.guesses))
    total_num_guesses += guesses

for word in longer_than_6:
    print(f'{word[0]}, {word[1]}\n{word[2]}')
print(stats_map)
print(total_num_guesses/list_length)
