# Swordle

## About
Swordle is a fun project I undertook to see if I could not only come up with a way to solve Wordle every time but to also find the best first guess to use.
A detailed exploration of this process and the results generated are available [here](https://josephmin.medium.com/spoiling-wordle-41a793da4d68).

Everything was run and tested using Python 3.8.2

## How To
To see how easiest to use this code, please see `test.py`.

## What's in the Box
* constants.py
  * This is pretty self-explanatory
* constraints.py
  * The constraints class. This is how I handle the information given by Wordle about previous guesses.
* guessers.py
  * The guessers classes. So far, this only includes the NaiveGuesser which simply runs down its ranked list of words and blindly picks the one with the highest rank that meets the constraints given. It takes the role of a user guessing words.
* swordle.py
  * The swordle class. This takes the role of a game instance that initializes with the solution and provides a checker for guesses which outputs new constraints for that guess as given by the online Wordle game.
* test.py
  * An example of how to guess for every word that is a possible solution for Wordle.
* train.py
  * Contains a function to score and rank a given list of words.
* utils.py
  * Also pretty self-explanatory.
* word_lists.py
  * Contains three lists:
  * The first is "legal_matches", which is a list of words that Wordle will accept as legal guesses that are NOT possible solutions to Wordle.
  * The second is "solutions", which is a list of words that Wordle used to use as possible solutions. This changed after the NYT acquisition.
  * The third is "new_solutions", which is the list that the new NYT version of Wordle uses.
