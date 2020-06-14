"""
The polar expedition graph!
===========================

Contains the graph connecting the vertices (or base stations) on the map.

This is going to be the main file that you are modifying. :)

Usage:
    Contains the graph, requires the connection to vertices and edges.
"""
import math
from vertex import Vertex
from edge import Edge


# Define a "edge already exists" exception
# Don't need to modify me.
class EdgeAlreadyExists(Exception):
    """Raised when edge already exists in the graph"""
    def __init__(self, message):
        super().__init__(message)


class Graph:
    """
    Graph Class
    -----------

    Represents the graph of vertices, which is equivalent to the map of base
    stations for our polar expedition.

    Attributes:
        * vertices (list): The list of vertices
    """

    def __init__(self):
        """
        Initialises an empty graph
        """
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        """
        Insert the vertex storing the y_pos and x_pos

        :param x_pos: The x position of the new vertex.
        :param y_pos: The y position of the new vertex.

        :type x_pos: float
        :type y_pos: float

        :return: The new vertex, also stored in the graph.
        """

        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        """
        Inserts the edge between vertex u and v.

        We're going to assume in this assignment that all vertices given to
        this will already exist in the graph.

        :param u: Vertex U
        :param v: Vertex V

        :type u: Vertex
        :type v: Vertex

        :return: The new edge between U and V.
        """

        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        """
        Removes the vertex V from the graph.
        :param v:  The pointer to the vertex to remove
        :type v: Vertex
        """

        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v)
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        """
        Get the distance between vertex u and v.

        :param u: A vertex to get the distance between.
        :param v: A vertex to get the distance between.

        :type u: Vertex
        :type v: Vertex
        :return: The Euclidean distance between two vertices.
        """

        # Euclidean Distance
        # sqrt( (x2-x1)^2 + (y2-y1)^2 )

        return math.sqrt(((v.x_pos - u.x_pos)**2) + ((v.y_pos - u.y_pos)**2))

    @staticmethod
    def opposite(e, v):
        """
        Returns the vertex at the other end of v.
        :param e: The edge to get the other node.
        :param v: Vertex on the edge.
        :return: Vertex at the end of the edge, or None if error.
        """

        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    ##############################################
    # Implement the functions below
    ##############################################

    def find_emergency_range(self, v):
        """
        Returns the distance to the vertex W that is furthest from V.
        :param v: The vertex to start at.
        :return: The distance of the vertex W furthest away from V.
        """
        #Solution 1 - Assumption: There might be vertices that are not connected. ie Split graph
        #Edges could have been removed, therefore need to test if still connected.
        #Doesn't pass a hidden test case.
        # furthestDist = 0
        # layers = self.bfs(v, 1000000)
        # for level in layers:
        #     for l in level:
        #         if furthestDist < self.distance(v, l):
        #             furthestDist = self.distance(v, l)

        #Solution 2 - Assumption: All vertices are connected.
        emergency_range = 0
        for vertex in self._vertices:
            distance = self.distance(v, vertex)
            if distance > emergency_range:
                emergency_range = distance
        
        return emergency_range

    def find_path(self, start_vertex, end_vertex, radius):
        """
        Find a path from vertex B to vertex S, such that the distance from B to
        every vertex in the path is within R.  If there is no path between B
        and S within R, then return None.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :return: The LIST of the VERTICES in the path.
        """
        #CHECK IF THERE IS A PATH
        end_vertex_present = False
        all_layers = self.BFS(start_vertex, radius)
        for layers in all_layers:
            for vertex in layers:
                if vertex == end_vertex:
                    end_vertex_present = True

        if end_vertex_present == False:
            return None

        #RETURNS A PATH (LIST)
        path = []
        temp = end_vertex

        while start_vertex not in path:
            path.insert(0, temp)
            temp = temp.parent

        return path

    def minimum_range(self, start, end):
        """
        Returns the minimum range required to go from Vertex B to Vertex S.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :return: The minimum range in the path to go from B to S.
        """
        #THE BARE MINIMUM THAT THE MIN_RANGE CAN BE IS THE DIRECT EUCLIDEAN RANGE
        #Assumption: Graph is connected. There is at least one path from start to end.
        all_ranges = []
        all_path = []
        mini = self.distance(start, end)
        all_ranges.append(mini)
        #------------------------------------------------------------------------

        #FINDING ONE PATH USING PREVIOUS EXAMPLE AND LARGE RADIUS
        radius = 1000000

        counter = 0
        #KEEP LOOPING TO FIND THE SHORTEST ROUTE
        while counter < 10:
            path = self.find_path(start, end, radius)
            if path is None:
                break
            #CHECKING BETW EACH VERTICE OF THAT PATH
            m = self.distance(start, end)
            i = 0
            while i + 1 < len(path):
                dist = self.distance(path[0], path[i+1])
                if dist > m:
                    m = dist
                i += 1

            radius = m - 0.01
            counter += 1
            #APPEND ALL PATHS INTO LIST
            all_path.append(path)

        #return m
            
        #------------------------------------------------------------------------
        #GET SHORTEST PATH
        s_path = all_path[-1]
        #APPEND ALL RANGES INTO A LIST AND GET MAXIMUM
        index = 0
        while index + 1 < len(s_path):
            distance = self.distance(s_path[0], s_path[index + 1])
            all_ranges.append(distance)
            index += 1

        return max(all_ranges)

    def move_vertex(self, v, new_x, new_y):
        """
        Move the defined vertex.

        If there is already a vertex there, do nothing.

        :param v: The vertex to move
        :param new_x: The new X position
        :param new_y: The new Y position
        """
        pos_taken = False
        for vertex in self._vertices:
            if vertex.x_pos == new_x and vertex.y_pos == new_y:
                pos_taken = True
        
        if pos_taken == False:
            v.move_vertex(new_x, new_y)

    #BREADTH FIRST SEARCH
    def BFS(self, start_vertex, radius):
        """
        Conducts a Breadth First Search to find all connecting vertices within the given radius.
        """
        #SETTING THINGS UP
        for vertex in self._vertices:
            vertex.seen = False
            vertex.parent = None

        start_vertex.seen = True
        all_layer = []
        current_layer = [start_vertex]
        next_layer = []
        empty = []

        #START OF BREADTH FIRST SEARCH
        while current_layer != empty:
            all_layer.append(current_layer)
            for element in current_layer:
                connected_vertices = []
                for edges in element.edges:
                    opp_vertex = self.opposite(edges, element)
                    if self.distance(start_vertex, opp_vertex) <= radius:
                        connected_vertices.append(opp_vertex)
                #GETTING NEXT LAYER & FORMING PATHS
                for vertex in connected_vertices:
                    if vertex.seen == False:
                        next_layer.append(vertex)
                        vertex.seen = True
                        if self.distance(start_vertex, vertex) <= radius:
                            vertex.parent = element 
            #UPDATE LAYERS
            current_layer = next_layer
            next_layer = []

        return all_layer

    #BREADTH FIRST SEARCH (SHORTEST PATH)
    def BFSS(self, start_vertex, radius):
        """
        Conducts a Breadth First Search to find the shortest path.
        """
        #SETTING THINGS UP
        for vertex in self._vertices:
            vertex.seen = False
            vertex.parentlist = []
            vertex.childlist = []

        start_vertex.seen = True
        all_layer = []
        current_layer = [start_vertex]
        next_layer = []
        empty = []

        #START OF BREADTH FIRST SEARCH
        while current_layer != empty:
            all_layer.append(current_layer)
            for element in current_layer:
                connected_vertices = []
                for edges in element.edges:
                    opp_vertex = self.opposite(edges, element)
                    if element not in opp_vertex.childlist:
                        connected_vertices.append(opp_vertex)
                #GETTING NEXT LAYER & FORMING PATHS
                for vertex in connected_vertices:
                    if vertex.seen == False:
                        next_layer.append(vertex)
                        vertex.seen = True
                        vertex.parentlist.append(element)
                        element.childlist.append(vertex)
                    if vertex.seen == True:
                        vertex.parentlist.append(element)
            #UPDATE LAYERS
            current_layer = next_layer
            next_layer = []

        return all_layer

