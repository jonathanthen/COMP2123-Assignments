from vertex import Vertex
from edge import Edge
from graph import Graph
import math

# Tolerance for the threshold of distances
TOLERANCE_THRESHOLD=0.001

def approx_value(a, b):
    """
    Asserts that the value of a and b are approximately close.
    :param a: A number to compare to.
    :param b: A number to compare against.
    :return: The bool if they're approximate
    """

    return math.isclose(a, b, abs_tol=TOLERANCE_THRESHOLD)

"""
Find the minimum range
          A
        / | \
        B  C  D
        / | /
        E   F
"""

G = Graph()

# Layer 1
A = G.insert_vertex(0, 0)

# Layer 2
B = G.insert_vertex(2, 0)
C = G.insert_vertex(2, 70)
D = G.insert_vertex(2, 99)

# Layer 3
E = G.insert_vertex(3, 3)
F = G.insert_vertex(4, 6)

# Make the edges
G.insert_edge(A, B)
G.insert_edge(A, C)
G.insert_edge(A, D)
G.insert_edge(C, E)
G.insert_edge(C, F)
G.insert_edge(D, F)


print(G.minimum_range(A, F))
print("----------------------")

G.move_vertex(F, 1, 1)
G.remove_vertex(C)
G.insert_edge(A, F)
print(G.minimum_range(A, F))

