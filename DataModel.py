"""
This module provides an abstraction for the data.
"""

import sys


class DataModel:

    def read_genres(self):
        """
        Reads the genre labels for the songs.
        """
        with open('data/genres.txt', 'r') as f:
            for line in f:
                track_and_genre = line.split()
                self.track_to_genre[track_and_genre[0]] = track_and_genre[1]

    def read_lyrics(self):
        """
        Has the lyric frequencies for a song.
        """
    
        with open('data/mxm_dataset_train.txt', 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                elif line.startswith('%'):
                    self.top_words = line[1:].split(',')
                else:
                    track = line.split(',')
                    track_id = track[0]
                    mxm_id = track[1]

                    word_freq_str = track[2:]
                    word_freq = {}
                    for word in word_freq_str:
                        id_and_count = word.split(':')
                        word_freq[int(id_and_count[0]) - 1] = int(id_and_count[1])   # One-indexing

                    self.track_to_lyrics[track_id] = word_freq

    def intersect_data(self):
        """
        Intersects the tracks that are found in both datasets.
        """

        common_tracks = set(self.track_to_genre.keys()).intersection(set(self.track_to_lyrics.keys()))

        not_in_genres = set(self.track_to_genre.keys()).difference(common_tracks)
        not_in_lyrics = set(self.track_to_lyrics.keys()).difference(common_tracks)

        for not_in_genre in not_in_genres:
            self.track_to_genre.pop(not_in_genre, None)

        for not_in_lyric in not_in_lyrics:
            self.track_to_lyrics.pop(not_in_lyric, None)

    def get_genres(self):
        """
        Returns the possible genres
        """
        return ['Pop_Rock', 'Electronic', 'Rap', 'Jazz', 'Latin', 'RnB', 'International', 'Country', 'Reggae', 'Blues', 'Vocal', 'Folk', 'New Age']


    def __init__(self):
        self.track_to_lyrics = {}
        self.track_to_genre = {}
        self.read_lyrics()
        self.read_genres()
        self.intersect_data()


