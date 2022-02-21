import json

from utils import write_frequency_dict_to_csv
# from word_lists import new_solutions

'''
Note:
### Frequency Dictionaries
Can build the character frequency dictionaries by position or just by absolute
number of occurences.
Can also build them by looking at both solutions and legal_matches or just solutions.
### Scored word list
* scored_solutions is the words and their respective scores from solutions
'''
def train_by_position(word_list):
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

    letter_by_position_counts = [{}, {}, {}, {}, {}]
    for w in word_list:
        for i in range(len(w)):
            l = w[i]
            letter_by_position_counts[i][l] = letter_by_position_counts[i].get(l, 0)+1

    write_frequency_dict_to_csv(letter_by_position_counts)

    scored_words = []
    for w in word_list:
        scored_words = insert_word_by_score(w, scored_words, letter_by_position_counts)
    return scored_words, letter_by_position_counts
