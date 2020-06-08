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

import random


class AlienInvasion:
    """
    Alien Invasion Class
    Contains three functions to be implemented:

    1. `is_sorted(A)` - returns whether the array is sorted.
    2. `count_markers(A, c)` - returns the number of indices `i` such that
                                | A[i] - i | <= c.
    3. `break_control(A, c)` - returns a "random" index that satisfies
                               |A[i] - i | <= c.
    """

    @staticmethod
    def is_sorted(A: list) -> bool:
        """
        Checks whether the given list of genetic code is sorted in
        increasing order.

        If the array (A) is None, return None.
        :param A: A list of indices.
        :return: True if sorted, else False.
        """
        #CHECK IF LIST IS NONE
        if A == None:
            return None
        #CHECK IF LIST IS EMPTY
        if len(A) == 0:
            return True
        #IF NOT, CHECK IF ITS SORTED    
        else:
            i = 1
            while i < len(A):
                current_value = A[0]
                to_check = A[i]
                #COMPARE PREVIOUS AND NEXT VALUE
                if current_value < to_check:
                    current_value = to_check
                #IF NEXT INDEX IS BIGGER THAN PREVIOUS, RETURN FALSE
                else:
                    return False
                i += 1
            #RETURN TRUE ONCE WHILE LOOP FINISHES
            return True

    def count_markers(self, A: list, c: int) -> int:
        """
        Counts the number of elements in A such that | A[i] - i | <= c

        If there are no numbers that satisfy the condition, return 0.
        If the array is None, return None.

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

        :param A: A **SORTED** array of integers in increasing order.
        :param c: The integer threshold
        :return: The number of elements that satisfy the condition.
        """

        #CHECK IF LIST IS NONE
        if A == None:
            return None
        #CHECK IF LIST IS EMPTY
        if len(A) == 0:
            return 0

        median = self.bS(A, 0, len(A)-1, c)
        if median != None:
            return self.rS(A, median, len(A)-1, c, median) - self.lS(A, 0, median, c, median) + 1
        else:
            return 0

        # linear_solution = self.count_markers_base_solution(A, c)
        # return linear_solution

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

        :param A: A **SORTED** list of integers in increasing order.
        :param c: The integer threshold.
        :return: The **INDEX** of an element that satisfies the condition.
        """
        #CHECK IF LIST IS NONE
        if A == None or len(A) == 0:
            return None

        #CHECK FIRST AND LAST ELEMENT FOR POSITIVE/NEGATIVE NUMBERS
        first = A[0]
        last = A[len(A) - 1]
        #INDEXES FOR START, END, MID
        start = 0
        end = len(A) - 1
        #KEEP AN INDEX
        index = -1
        #count = 0

        #POSITIVE VALUES ONLY
        if first >= 0 and last >= 0:
            #ITERATION
            while start <= end:
                mid = (start + end)//2
                if abs(A[mid] - mid) <= c:
                    #count = mid + 1
                    index = mid
                    start = mid + 1
                else:
                    end = mid - 1

            if index == -1:
                return None
            else:
                return random.choice([x for x in range(0, index+1)])

        #NEGATIVE VALUES ONLY
        elif first <= 0 and last <= 0:
            #ITERATION
            while start <= end:
                mid = (start + end)//2
                if abs(A[mid] - mid) <= c:
                    #count = len(A) - mid
                    index = mid
                    end = mid - 1
                else:
                    start = mid + 1
            if index == -1:
                return None
            else:
                return random.choice([x for x in range(index, len(A))])

        #POSITIVE & NEGATIVE VALUES (first < 0 and last > 0)
        else:
            #SET THE VALUES OF START AND END
            start = 0
            end = len(A) - 1
            mid = (start + end)//2
            #ITERATION TO FIND LOWER BOUND
            left_index = -1
            while start <= end:
                mid = (start + end)//2
                if abs(A[mid] - mid) <= c:
                    if left_index == -1:
                        left_index = mid
                    elif abs(A[left_index] - left_index) == 0:
                        left_index = mid
                    elif abs(A[mid] - mid) >= abs(A[left_index] - left_index):
                        left_index = mid
                    end = mid - 1
                else:
                    if A[mid] - mid >= 0:
                        end = mid - 1
                    else:
                        start = mid + 1

            #RESET THE VALUES OF START AND END
            start = 0
            end = len(A) - 1
            mid = (start + end)//2
            #ITERATION TO FIND UPPER BOUND
            right_index = -1
            while start <= end:
                mid = (start + end)//2
                if abs(A[mid] - mid) <= c:
                    if right_index == -1:
                        right_index = mid
                    elif abs(A[right_index] - right_index) == 0:
                        right_index = mid
                    elif abs(A[mid] - mid) <= abs(A[right_index] - right_index):
                        right_index = mid
                    start = mid + 1
                else:
                    if A[mid] - mid >= 0:
                        end = mid - 1
                    else:
                        start = mid + 1  

            print(left_index, right_index)
            if left_index == -1 and right_index == -1:
                return None
            else:
                return random.choice([x for x in range(left_index, right_index + 1)])
            
        # linear_solution = self.break_control_base_solution(A, c)
        # return linear_solution

    def count_markers_base_solution(self, A: list, c: int) -> int:
        """
        RETURNS A O(n) SOLUTION FOR COUNT_MARKERS
        """

        #CHECK IF ARRAY IS NONE
        if A == None:
            return None

        #O(n) SOLUTION
        index = 0
        count = 0
        while index < len(A):
            if abs(A[index] - index) <= c:
                count += 1
            index += 1

        return count

    def break_control_base_solution(self, A: list, c: int) -> int:
        """
        RETURNS A O(n) SOLUTION FOR BREAK_CONTROL
        """
        #CHECK IF ARRAY IS NONE OR EMPTY
        if A == None or len(A) == 0:
            return None
        
        #O(n) SOLUTION
        l = []
        index = 0

        while index < len(A):
            if abs(A[index] - index) <= c:
                l.append(index)
            index += 1
        
        if len(l) == 0:
            return None

        return random.choice(l)

    def bS(self, A, start, end, c):
        if end >= start:
            mid = start + (end-start)//2
            if abs(A[mid]-mid) <= c:
                return mid
            else:
                if mid == start or mid == end:
                    return None
                elif abs(A[mid]-mid) > abs(A[mid+1]-(mid+1)):
                    return self.bS(A, mid+1, end, c)
                else:
                    return self.bS(A, start, mid-1, c)
        else:
            return None

    def lS(self, A, start, end, c, left):
        if end >= start:
            mid = start + (end - start)//2
            if abs(A[mid]-mid) <= c:
                left = mid
                return self.lS(A, start, mid-1, c, left)
            else:
                return self.lS(A, mid+1, end, c, left)
        else:
            return left

    def rS(self, A, start, end, c, right):
        if end >= start:
            mid = start + (end - start)//2
            if abs(A[mid] - mid <= c):
                right = mid
                return self.rS(A, mid+1, end, c, right)
            else:
                return self.rS(A, start, mid-1, c, right)
        else:
            return right