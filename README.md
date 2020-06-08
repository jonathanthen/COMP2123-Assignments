# Alien Invasion

**Story**

Unbeknownst to the people on Earth, an alien invasion has been going on for years, setting certain genetic markers in order to brainwash them to do the alien's bidding. Recently, this plot was discovered and scientists are now rushing to find out how prevalent this problem is. They have developed an oddly specific test based on the genetic markers that the aliens use for their mind control.

This test involves putting the genetic markers in sorted order and checking whether, for sufficiently many indices, the value at that index is too close to said index, indicating that it was artificially set. If a person is being controlled by the aliens, we aim to break the aliens' influence by reverting one of the genetic markers. To make it harder for the aliens to counteract this procedure, we need to pick a random genetic marker that they modified. 

Your job is to help write the required algorithms to perform these tasks and save the human race, before all hope is lost! Good luck! The fate of humanity rests on your shoulders... 

About the code

Implement the functions in invasion.py where all the code for this assignment resides. 

Invasion.py

is_sorted(A: list) -> bool

    Arguments:

        A: A list of integers

    Returns:

        boolean (True, False or None if A is None)

Returns whether the integers stored in A are sorted in increasing order.

count_markers(A: list, c: int) -> int

* Arguments
    * A: Genetic Markers (a sorted list of integers)
    * c: an integer threshold.

* Returns:
    * integer : The number of markers that satisfy the condition.
        * Note: when A is None, then return None

Returns the number of indices i such that

∣A[i]−i∣≤c

Where i is the index of the element in array A. 

Important: The implementation should be a divide-and-conquer algorithm that runs in O(log n) time.
```
break_control(A: list, c: int) -> int
```

Arguments

* A: Genetic Markers (a sorted list of integers)
* c: an integer threshold

Returns:

* Integer: A random index of a number that satisfies the condition.
    * Note: when A is None, then return None
    * If there is no index that can be returned, then return None.

Returns a random index i that satisfies:

∣A[i]−i∣≤c

Important: The implementation should be a divide-and-conquer algorithm that runs in O(log n) time.

About the testing

We will be doing git submissions to submit the work to be unit tested.

Correctness

* Your code should produce the outcome expected by the input we give.
* It should handle cases defined above including the use of None.

Efficiency/Complexity

* We will be testing that your code runs according to the complexities defined.
* Divide and conquer is expected to run in O(log n) time.
* An array loop is O(n) time.

Type of tests:

* public: Tests that you, the students, are able to see with full visibility. You can see (a) the name, (b) the score of the test, and (c) the result.

* hidden: Tests that you, the students, can partially see - you can see (a) the outcome of the hidden unit test (pass/fail).

    * Similar to what we had on Assignment 4. :)
