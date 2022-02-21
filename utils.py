import string

def write_frequency_dict_to_csv(
    letter_by_position_counts,
    filepath='results/letter_frequences_by_position.csv'):
    with open(filepath, 'w') as f:
        csv_columns = ['Letter', 'Position 1', 'Position 2', 'Position 3', 'Position 4', 'Position 5']
        f.write(', '.join(csv_columns))
        f.write('\n')
        for l in string.ascii_lowercase:
            row = [
                l,
                str(letter_by_position_counts[0].get(l, 0)),
                str(letter_by_position_counts[1].get(l, 0)),
                str(letter_by_position_counts[2].get(l, 0)),
                str(letter_by_position_counts[3].get(l, 0)),
                str(letter_by_position_counts[4].get(l, 0))
            ]
            f.write(', '.join(row))
            f.write('\n')
