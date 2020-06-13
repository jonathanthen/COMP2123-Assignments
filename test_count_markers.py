"""
This module focuses on testing the `count_markers` function.

Please note: These are only EXAMPLE tests, you will need to extend and
think of corner cases to allow for further testing.
"""

import unittest

from invasion import AlienInvasion

class CountMarkersTests(unittest.TestCase):

    def test_count_markers_small_array(self):

        V = AlienInvasion()

        markers = [0, 1, 2, 3, 4, 5, 6, 8, 18, 20]
        c = 2

        res = V.count_markers(markers, c)

        assert res == 8, "Incorrect number of markers returned " \
                         "Expected 8, Got: {}".format(res)

    def test_count_markers_large_array(self):
        V = AlienInvasion()

        markers = [x for x in range(20, 300, 3)]

        c = 35

        res = V.count_markers(markers, c)

        assert res == 8, "Incorrect number of markers returned, " \
                         "Expected 8, got {}".format(res)

    def test_count_negatives(self):

        V = AlienInvasion()

        markers = [x for x in range(-20, -2, 3)]

        c = 15

        res = V.count_markers(markers, c)

        assert res == 3, "Incorrect number of markers returned, " \
                         "Expected 3, got {}".format(res)

