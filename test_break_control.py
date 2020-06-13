"""
This module focuses on testing the `break_control` function.

Please note: These are only EXAMPLE tests, you will need to extend and
think of corner cases to allow for further testing.
"""

import unittest

from invasion import AlienInvasion

class BreakControlTests(unittest.TestCase):

    def test_break_control_small_array(self):

        V = AlienInvasion()

        markers = [0, 1, 2, 3, 4, 5, 6, 8, 18, 20]
        c = 2

        res = V.break_control(markers, c)

        assert res is not None, "The result should not be None"

        lower_index = 0
        upper_index = 7

        assert lower_index <= res <= upper_index, "The index you returned was" \
                                                  "not within the bounds."


    def test_break_control_large_array(self):
        V = AlienInvasion()

        markers = [x for x in range(20, 300, 3)]

        c = 35

        res = V.break_control(markers, c)

        assert res is not None, "The result should not be None"

        lower_index = 0
        upper_index = 7

        assert lower_index <= res <= upper_index, "The index you returned was" \
                                                  "not within the bounds."


    def test_break_control_negatives(self):

        V = AlienInvasion()

        markers = [x for x in range(-20, -2, 3)]

        c = 15

        res = V.break_control(markers, c)

        assert res is not None, "The result should not be None"

        lower_index = 3
        upper_index = 5

        assert lower_index <= res <= upper_index, "The index you returned was" \
                                                  "not within the bounds."

