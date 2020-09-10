from unittest import TestCase

from main import csv_filler, sorter_by_last_name, binary_search

filled_players = csv_filler(filename='chess-players.csv')
sorted_players = sorter_by_last_name(filled_players)


class Test(TestCase):

    def test_csv_filler(self):
        self.assertGreater(len(filled_players), 0, "filled players list shouldn't be null")

    def test_sorter_by_last_name(self):
        self.assertGreater(len(sorted_players), 0,
                           "sorted players list shouldn't be null")
        self.assertEqual("Aaron", sorted_players[1].last_name,
                         "Player's last name should be Aaron")

    def test_binary_search(self):
        self.assertEqual("Aagaard",
                         (binary_search(sorted_players, "Aagaard"))[0].last_name)
