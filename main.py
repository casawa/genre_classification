"""
This module aims to perform the main
training.
"""

import sys




def read_lyrics_dataset():
    """
    Has the lyric frequencies for a song.
    """

    with open('data/mxm_dataset_train.txt', 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            elif line.startswith('%'):
                top_words = line[1:].split(',')
            else:
                

def main():

    read_lyrics_dataset()




if __name__ == "__main__":
    main()




