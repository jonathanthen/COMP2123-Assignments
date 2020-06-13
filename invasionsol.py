"""
Alien Invasion
--------------
Your job is to help write the required algorithms to perform these tasks and
save the human race, before all hope is lost! Good luck!
The fate of humanity rests on your shoulders...
--------------

This module will contain all functions that you must implement. It will serve
as the main file to be created during testing.

Usage:
    - Contains functions that will be implemented to stop the Alien Invasion!
"""

import math
import random


class AlienInvasion:
    """
    Alien Invasion Class
    Contains three functions to be implemented:

    1. `is_sorted(A)` - returns whether the array is sorted.
    2. `count_markers(A, c)` - returns the number of indicies `i` such that
                                | A[i] - i | <= c.
    3. `break_control(A, c)` - returns a "random" index that satisfies
                               |A[i] - i | <= c.
    """

    @staticmethod
    def is_sorted(A: list) -> bool:
        """
        Checks whether the given list of genetic code is sorted in
        non-decreasing order.

        If the array (A) is None, return None.
        :param A: A list of indices.
        :return: True if sorted, else False.
        """

        # If it's None, return None
        if A is None:
            return None

        # If the length is 0 or 1, then
        # it's sorted
        if len(A) <= 1:
            return True

        # If not, let's loop through
        curr = A[0]

        for i in range(1, len(A)):
            val = A[i]

            # Strictly increasing - so >=
            # If it was non-decreasing, then >
            if curr >= val:
                return False
            curr = val

        return True

    def get_bounds(self, A: list, c: int) -> (int, int):
        """
        Get boundary values

        This will provide L and H, where L is the lowest index
        of a number where |A[i] - i | <= c.

        H is the highest index of the number where |A[i] - i| <= c

        :param A: A **Sorted** array of integers in increasing order.
        :param c: The integer threshold.
        :returns: (int, int) the upper and lower indices.
        """

        # This implementation uses two binary search algorithms to find
        # the upper and lower bound.
        # First step is to isolate the upper_bound.

        L = 0
        R = len(A)
        while L < R:
            # Find the middle value
            m = math.floor((L + R) / 2)
            v = A[m]

            # Check if |A[i] - i| < c:
            if abs(v - m) > c:
                # This step is important, if we are on a negative number
                # We need to move right instead of left.
                if v < 0 or (v - m) < 0:
                    L = m + 1
                else:
                    # Else, we need to move towards the left.
                    R = m
            else:
                # If it matches the condition, move the left up because we're
                # going towards the lowest number.
                L = m + 1
        upper_bound = R

        # Now that we have the upper bound, we only need to
        # Binary search for the lower bound between index 0 and upper_bound.
        L = 0
        R = upper_bound
        while L < R:
            # find the middle
            m = math.floor((L + R) / 2)
            if abs(A[m] - m) > c:
                # If it's greater, move the left up.
                L = m + 1
            else:
                # Else, move the right down.
                R = m

        # Finally we have the lower bound.
        lower_bound = L

        # Return the lower bound and the upper bound index
        # Note the -1 because the upper bound will give the
        # size of the array in worst case.
        return lower_bound, upper_bound - 1

    def count_markers(self, A: list, c: int) -> int:
        """
        Counts the number of elements in A such that | A[i] - i | <= c

        If there are no numbers, return 0.
        If the array is invalid or None, return None.

        Example:

        A = [1, 2, 4, 8, 16, 32, 64]
        c = 4

        A[0] = | 1 - 0 |  = 1.
        A[1] = | 2 - 1 |  = 1.
        A[2] = | 4 - 2 |  = 2.
        A[3] = | 8 - 3 |  = 5.
        A[4] = | 16 - 4 | = 12.
        A[5] = | 32 - 5 | = 27.
        A[6] = | 64 - 6 | = 58.

        AlienInvasion.count_markers(A, c) -> 3

        :param A: A **SORTED** array of integers.
        :param c: The integer threshold
        :return: The number of elements that satisfy the condition.
        """

        # Corner cases
        if A is None:
            return None

        if len(A) == 0:
            return 0

        # If it's 1 element long, check if it satisfies the condition.
        if len(A) == 1:
            return 1 if A[0] <= c else 0

        # Get the bounds
        bounds = self.get_bounds(A, c)

        # Return the number (+1 here for index starting at 0)
        return bounds[1] - bounds[0] + 1

        # ==========================
        # brute-force O(n) approach?
        # You can ignore me.
        # ==========================

        # arr_to_return = []
        # indices = []
        # for idx, val in enumerate(A):
        #     if abs(val - idx) <= c:
        #         arr_to_return.append(val)
        #         indices.append(idx)

        # Indices is testing that we don't have two
        # separate ranges for datasets.
        # (e.g. if there's a split in the middle..)
        # for i in range(1, len(indices)):
        #     assert indices[i] == indices[i-1] + 1

        # # DEBUG PLS!
        # # print("Array: ", arr_to_return)
        # # print("Indices: ", indices)

        # return len(arr_to_return)

    def break_control(self, A: list, c: int) -> int:
        """
        Returns a **random** index such that A[i] satisfies:
            | A[i] - i | <= c

        If there are no numbers/indices that satisfy the conditions, or if
        the array is None, return `None`.

        Example:

        A = [1, 2, 4, 8, 16, 32, 64]
        c = 4

        A[0] = | 1 - 0 |  = 1.
        A[1] = | 2 - 1 |  = 1.
        A[2] = | 4 - 2 |  = 2.
        A[3] = | 8 - 3 |  = 5.
        A[4] = | 16 - 4 | = 12.
        A[5] = | 32 - 5 | = 27.
        A[6] = | 64 - 6 | = 58.

        AlienInvasion.break_control(A, c)

        Will return either: 0, 1 or 2.

        :param A: A **SORTED** list of integers.
        :param c: The integer threshold.
        :return: The **INDEX** of an element that satisfies the condition.
        """

        # If it's none, then return None
        if A is None:
            return None

        # If empty array, no numbers so return None
        if len(A) == 0:
            return None

        # Get the bounds
        lower_bound, upper_bound = self.get_bounds(A, c)

        # Check if there are no numbers, return none
        if (upper_bound - lower_bound) + 1 == 0:
            return None

        # Return the random index
        if lower_bound == upper_bound:
            return lower_bound

        # Return a ``RANDOM`` between upper and lower.
        return random.randrange(lower_bound, upper_bound)

        # ================
        # BR00T FORCE
        # ================

        # indices = []
        # for idx, val in enumerate(A):
        #     if abs(val - idx) <= c:
        #         indices.append(idx)

        # if len(indices) == 0:
        #     return None

        # for i in range(1, len(indices)):
        #     assert indices[i] == indices[i-1] + 1

        # if len(indices) == 1:
        #     return indices[0]

        # return random.randrange(indices[0], indices[-1])