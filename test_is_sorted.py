"""
This module tests the basic functionality of `is_sorted` on the
`invasion.py`.

Please note: These are only EXAMPLE tests, you will need to extend and
think of corner cases to allow for further testing.
"""

import unittest

from invasion import AlienInvasion

class IsSortedTests(unittest.TestCase):

    def test_simple_array_sorted(self):
        """
        Checks whether you can detect an already-sorted array.
        """

        a = [x for x in range(0, 9)]

        assert AlienInvasion.is_sorted(a) is True, "A sorted array should" \
                                                   "return True!"

    def test_simple_array_unsorted(self):
        """
        Checks whether you can detect an unsorted array.
        """
        a = [1, 6, 5, 2, 3, 7, 4]

        assert AlienInvasion.is_sorted(a) is False, "An unsorted array should" \
                                                    "return True!"

    def test_reverse_sorted(self):
        """
        Tests reverse sorted arrays.
        """

        a = [x for x in range(1, 100)]

        assert AlienInvasion.is_sorted(a) is True, "A sorted array should" \
                                                   "return True!"
        a.reverse()

        assert AlienInvasion.is_sorted(a) is False, "A reverse sorted array " \
                                                    "should return False!"

    def test_should_return_none(self):
        """
        Test that you return None when you're given None
        """

        a = None

        assert AlienInvasion.is_sorted(a) is None, "You should return None " \
                                                   "when A is None"

    def test_dealing_with_negatives(self):
        """
        Test you can check negative numbers
        """

        a = [x for x in range(-70, -10)]

        assert AlienInvasion.is_sorted(a) is True, "Sorted array should " \
                                                   "return True"

