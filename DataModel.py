"""
This module provides an abstraction for the data.
"""

import sys
import numpy as np

class DataModel:

    def read_genres(self):
        """
        Reads the genre labels for the songs.
        """
        with open('data/genres.txt', 'r') as f:
            for line in f:
                track_and_genre = line.strip('\n').split('\t')
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
        return sorted(['Pop_Rock', 'Electronic', 'Rap', 'Jazz', 'Latin', 'RnB', 'International', 'Country', 'Reggae', 'Blues', 'Vocal', 'Folk', 'New Age'])

    def get_genre_to_index(self):
        """
        Returns a map from a genre's name to its index in the list of genres.
        """
        genres = sorted(['Pop_Rock', 'Electronic', 'Rap', 'Jazz', 'Latin', 'RnB', 'International', 'Country', 'Reggae', 'Blues', 'Vocal', 'Folk', 'New Age'])
        genre_to_index = {}
        for i, genre in enumerate(genres):
            genre_to_index[genre] = i

        return genre_to_index


    def create_X(self, tracks):
        """
        Given the track IDs, creates the X matrix for those tracks
        """
        X = np.zeros((len(tracks), len(self.top_words)))
        for i, track in enumerate(tracks):
            features = self.track_to_lyrics[track]
            for feature in features:
                X[i][feature] = features[feature]

        return X

    def create_y(self, tracks):
        """
        Given the track IDs, creates the y matrix for those tracks
        """   
        genre_to_index = self.get_genre_to_index()
        
        y = np.zeros((len(tracks), len(genre_to_index)))
        for i, track in enumerate(tracks):
            category = genre_to_index[self.track_to_genre[track]]
            y[i][category] = 1

        return y

    def create_training_test_sets(self):
        """
        Creates training and test sets for classification.
        """
        tracks = self.track_to_genre.keys()
        train_tracks = tracks[:24000]
        test_tracks = tracks[24000:30000]

        self.train_X = self.create_X(train_tracks)
        self.test_X = self.create_X(test_tracks)

        self.train_y = self.create_y(train_tracks)
        self.test_y = self.create_y(test_tracks)

    def __init__(self):
        self.track_to_lyrics = {}
        self.track_to_genre = {}
        self.read_lyrics()
        self.read_genres()
        self.intersect_data()
        self.create_training_test_sets()


