"""
Vertex Module
============

Represents a vertex in the data structure.
Contains the information that places the object in the graph.

Usage:
    Not to be run as main, is used as an import for the graph.
    Contains information about the vertex/nodes in the graph.

Example:
    v = Vertex(x_pos, y_pos)
"""


class Vertex:
    """
    Vertex Class
    -------------

    Represents an object on the map, with an X position and Y position.

    Attributes:
        * x_pos (float): The X position of the vertex.
        * y_pos (float): The Y position of the vertex.
        * edges (list) : The list of edges where this node is connected.
    """

    def __init__(self, x_pos, y_pos):
        """
        Initialises the vertex on the map. We need our base stations to belong
        somewhere!

        Params:
            :param x_pos: The X position of this vertex, can be -infinity <=
                        x_pos <= infinity
            :param y_pos: The Y position of this vertex, can be -infinity <=
                        y_pos <= infinity

        Argument Types:
            :type x_pos: float
            :type y_pos: float
        """

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.edges = []

    def __eq__(self, other):
        """
        Overriding the equality, no need to touch :)
        :param other: The other object comaparing to.
        :return: Bool if equal
        """

        # If it's the same instance.
        if isinstance(other, Vertex):
            return other.x_pos == self.x_pos and other.y_pos == self.y_pos
        return False

    def __ne__(self, other):
        """
        Implementing the not equal method.
        (vertex != other vertex)
        :param other: The other object to compare to.
        :return: The bool if not equal.
        """

        # If it's the same instance.
        if isinstance(other, Vertex):
            # It should not have same coords
            return other.x_pos != self.x_pos or other.y_pos != self.y_pos

        return True

    def __repr__(self):
        return "V({}, {})".format(self.x_pos, self.y_pos)

    def __hash__(self):
        return hash(repr(self))

    def add_edge(self, e):
        """
        Adds the edge e to the set of edges.
        :param e: The new edge to add.
        """
        self.edges.append(e)

    def remove_edge(self, e):
        """
        Removes the edge from the set of edges.
        :param e: The edge to remove.
        """
        self.edges.remove(e)

    ##############################################
    # Implement the functions below
    ##############################################

    def move_vertex(self, x_pos, y_pos):
        """
        Sets the new position of the vertex.
        Since our base stations are on ice-burgs, we assume that their location
        can change.
        Params:
            :param x_pos: The new X position of the vertex.
            :param y_pos: The new Y position of the vertex.

        Argument Types:
            :type x_pos: float
            :type y_pos: float
        """

        self.x_pos = x_pos
        self.y_pos = y_pos