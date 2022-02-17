import json

from word_lists import legal_matches
from word_lists import solutions

'''
Note:
### Frequency Dictionaries
Can build the character frequency dictionaries by position or just by absolute
number of occurences.
Can also build them by looking at both solutions and legal_matches or just solutions.
### Scored word lists
Should output two scored lists though:
* scored_solutions is just words and scores from word_lists.solutions
* scored_all_words is words and scores for all words (solutions and matches)
'''
def train_by_position(score_matches=False, output_matches=False):
    def score_word(word, letter_by_position_counts):
        score = 0
        # Naively/linearly sum the number of occurrences of that letter in that
        # position to the score
        for i in range(len(word)):
            c = word[i]
            score += letter_by_position_counts[i].get(c, 0)
        return score

    def insert_word_by_score(word, scored_words, letter_by_position_counts):
        word_and_score = (w, score_word(w, letter_by_position_counts))
        insert_index = 0
        for i in range(len(scored_words)):
            current_score = scored_words[i][1]
            insert_index = i
            if i == len(scored_words)-1:
                if word_and_score[1] <= current_score:
                    insert_index = insert_index+1
                break
            next_score = scored_words[i+1][1]
            if word_and_score[1] > current_score:
                break
            if word_and_score[1] <= current_score and word_and_score[1] > next_score:
                insert_index = insert_index+1
                break
        scored_words.insert(insert_index, word_and_score)
        return scored_words

    print('Generating character frequency dictionary by position for solution words.')
    letter_by_position_counts = [{}, {}, {}, {}, {}]
    for w in solutions:
        for i in range(len(w)):
            l = w[i]
            letter_by_position_counts[i][l] = letter_by_position_counts[i].get(l, 0)+1
    if score_matches:
        print('Generating character frequency dictionary by position for legal matches.')
        for w in legal_matches:
            for i in range(len(w)):
                l = w[i]
                letter_by_position_counts[i][l] = letter_by_position_counts[i].get(l, 0)+1

    if output_matches:
        print('Generating and sorting scores for all words.')
        scored_all_words = []
        for w in solutions:
            scored_all_words = insert_word_by_score(w, scored_all_words, letter_by_position_counts)
        for w in legal_matches:
            scored_all_words = insert_word_by_score(w, scored_all_words, letter_by_position_counts)
        return scored_all_words

    print('Generating and sorting scores for solutions words.')
    scored_words = []
    for w in solutions:
        scored_words = insert_word_by_score(w, scored_words, letter_by_position_counts)
    return scored_words



def train_by_absolute_frequency(score_matches=False, output_matches=False):
    def score_word(word, letter_counts):
        score = 0
        for c in word:
            score += letter_counts.get(c, 0)
        return score

    def insert_word_by_score(word, scored_words, letter_counts):
        word_and_score = (w, score_word(w, letter_counts))
        insert_index = 0
        for i in range(len(scored_words)):
            current_score = scored_words[i][1]
            insert_index = i
            if i == len(scored_words)-1:
                if word_and_score[1] <= current_score:
                    insert_index = insert_index+1
                break
            next_score = scored_words[i+1][1]
            if word_and_score[1] > current_score:
                break
            if word_and_score[1] <= current_score and word_and_score[1] > next_score:
                insert_index = insert_index+1
                break
        scored_words.insert(insert_index, word_and_score)
        return scored_words

    letter_counts = {}
    for w in solutions:
        for i in range(len(w)):
            l = w[i]
            letter_counts[l] = letter_counts.get(l, 0)+1
    if score_matches:
        print('Generating character frequency dictionary by position for legal matches.')
        for w in legal_matches:
            for i in range(len(w)):
                l = w[i]
                letter_counts[l] = letter_counts.get(l, 0)+1

    if output_matches:
        print('Generating and sorting scores for all words.')
        scored_all_words = []
        for w in solutions:
            scored_all_words = insert_word_by_score(w, scored_all_words, letter_counts)
        for w in legal_matches:
            scored_all_words = insert_word_by_score(w, scored_all_words, letter_counts)
        return scored_all_words

    print('Generating and sorting scores for solutions words.')
    scored_words = []
    for w in solutions:
        scored_words = insert_word_by_score(w, scored_words, letter_counts)
    return scored_words
