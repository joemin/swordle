from multiprocessing import Pool

from word_lists import new_solutions
import guessers, swordle

def guess_for_word(word):
    guesser = guessers.NaiveGuesser(new_solutions)
    game = swordle.Swordle(word)
    print(word)

    solution_found = False
    guesses = 0
    while not solution_found and guesses <= 10:
        guesses += 1
        next_guess = guesser.next_guess()
        if game.is_solution(next_guess):
            solution_found = True
        guesser.update_constraints(next_guess, game.check_guess(next_guess))
        guesser.update_scored_words_with_constraints()

    return (word, guesses)
    # return (word, guesses, guesser.guesses)

if __name__ == '__main__':
    word_list = new_solutions
    guess_list = []
    with Pool(10) as p:
        guess_list = p.map(guess_for_word, word_list)


    losses = []
    for guess in guess_list:
        if guess[1] > 6:
            losses.append(guess)
    guess_nums = [guess[1] for guess in guess_list]

    print(f'Average number of guesses: {sum(guess_nums)/len(guess_nums)}')
    print(f'Losses: {losses}')
