"""
This module processes the data in a more
convenient fashion for the algorithms.
"""

import sys

raw_data_file = ''
formatted_data_file = ''

"""
Using the Porter Stemmer algorithm, this function
stems words to count words with the same stem
as the same word
"""
def stem_words():
    # Use porter stemmer

"""
This function removes stop words (common words),
which are typically not very insightful due to 
their high frequency in a variety of settings
"""
def remove_stop_words():


"""
Reads the raw data
"""
def read_data():
    with open(raw_data_file, 'r') as f:


"""
Writes the formatted data
"""
def write_data():

    with open(formatted_data_file, 'w') as f:


def main():
    read_data()
    remove_stop_words()
    stem_words()
    write_data()

if __name__ == '__main__':
    main()

