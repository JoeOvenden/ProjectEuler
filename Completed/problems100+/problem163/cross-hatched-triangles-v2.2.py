import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_N_primes, binary_search
from bisect import insort
from time import time

# Runtime: approximately 100 seconds

PRIMES = get_N_primes(3997)     # One prime for every node in the size 36 triangle
SOLUTION_IDS = []               # Unique identifiers for each triangle found
ANALYSE = False                 # Setting for printing various things about the triangle


# Enum for the two types of size 1 triangles, see documentation.
class TriangleType:
    FLAT = 0
    UPSIDE_DOWN = 1


# Class for each vertex in the hatched triangle
class Node:
    id = 0

    def __init__(self):
        # elements in adjacent_nodes are as such: [node, angle]
        self.id = Node.id
        self.id_prime = PRIMES[self.id] # Unique prime identifier
        Node.id += 1
        self.adjacent_nodes = []    # All the nodes that are directly adjacent
        self.lines = []             # All the lines that the node is on


    def isConnected(self, node):
        # Returns true if self and node are connected by a straight line, otherwise false
        for line in self.lines:
            if node.on_line(line):
                return True
        return False


    def add_adjacent(self, node, angle):
        # Checks that node is not already in self.adjacant_nodes and if not, adds it
        alreadyInList = False
        for [adjacent_node, adjacent_node_angle] in self.adjacent_nodes:
            if adjacent_node.id == node.id:
                alreadyInList = True

        # If not already in the list then add it
        if not alreadyInList:
            self.adjacent_nodes.append([node, angle])


    def on_line(self, line):
        # Returns true if the node is on the line, otherwise false
        for L in self.lines:
            if L.id == line.id:
                return True
        return False


# Class for all size 1 triangles in the hatched triangle
class Triangle:
    id = 0

    def __init__(self, type):
        self.id = Triangle.id
        Triangle.id += 1

        self.nodes = []     # List of nodes in the triangle
        self.type = type    # TriangleType.FLAT or TriangleType.UPSIDE_DOWN


    def add_edge(self, index1, index2, angle):
        """
        Upside down triangles are essentially flat triangles that have been reflected
        horizontally, in the sense that their nodes are numbered in this way
        as such, the angles are equal to 180 - angle (mod 180).
        See documentation.
        """
        node1, node2 = self.nodes[index1], self.nodes[index2]

        # Convert angle so that it is appropriate for an upside down triangle
        if self.type == TriangleType.UPSIDE_DOWN:
            angle = (180 - angle) % 180
        node1.add_adjacent(node2, angle)
        node2.add_adjacent(node1, angle)


    def add_edges(self):
        """
        Connects all nodes that should be connected together with their respective angles
        Note: add_edge handles the angle adjustment for upside down triangles
        See documentation.
        """
        self.add_edge(0, 1, 0)
        self.add_edge(0, 2, 150)
        self.add_edge(0, 3, 120)
        self.add_edge(1, 4, 0)
        self.add_edge(1, 2, 90)
        self.add_edge(2, 4, 30)
        self.add_edge(2, 5, 150)
        self.add_edge(2, 6, 90)
        self.add_edge(2, 3, 30)
        self.add_edge(3, 6, 120)
        self.add_edge(4, 5, 60)
        self.add_edge(5, 6, 60)


    def add_new_node(self, node):
        # Appends new node to triangle node list
        self.nodes.append(node)

    def insert_node(self, index, node):
        # Inserts a node a specific index in the triangle node list
        self.nodes.insert(index, node)

"""
Class for each layer of triangles in the cross hatched triangle.
Cross hatched triangle is made starting with a size 1 triangle and addind layers.
Adding a layer to a size n triangle creates a size n+1 triangle.
See documentation
"""
class Layer:
    id = 0
    
    def __init__(self):
        self.id = Layer.id
        Layer.id += 1
        self.triangles = []     # List of triangles in the layer

    
    def get_triangle(self,index):
        # Returns the triangle at a specific index within the layer
        return self.triangles[index]


    def add_triangle(self,triangle):
        # Adds triangle to the triangle list
        self.triangles.append(triangle)


# Class for each fully extended straight line within the hatched triangle
class Line:
    ID = 0
    def __init__(self, start_node, angle):
        self.start_node = start_node    # Line start node
        self.end_node = None            # Line end node
        self.nodes = []                 # List of nodes on the line
        self.angle = angle              # Angle of line
        self.id = Line.ID
        Line.ID += 1


    def set_end_node(self, node):
        self.end_node = node

    def add_node(self, node):
        self.nodes.append(node)     # Add node to the line's list of nodes
        node.lines.append(self)     # Add line to the node's list of lines which it is on

"""
Class for the cross hatched triangle. 
The hatched triangle is constructed starting with a size 1 triangle and then adding
layers of triangles one by one. For instance to get from a size 1 triangle to a size
36 triangle, 35 layers need to be added. See documentation.
"""
class Hatched_Triangle:
    def __init__(self):
        self.layers = []                # List of layers
        self.nodes = []                 # List of nodes
        self.processed_node_ids = []    # TODO
        self.zero_nodes = []            # List of zero nodes, see documentation
        self.lines = []                 # List of fully extended lines
        self.zero_lines = []            # List of zero lines, see documentation
        self.layer_count = 0            # Count of existing number of layers


    def reset(self):
        # Resets the hatched triangle. 
        Line.ID = 0
        Layer.id = 0
        Triangle.id = 0
        Node.id = 0
        SOLUTION_IDS = []


    def analyse(self):
        # Prints various things including zero lines, lines, triangle solutions
        print("zero nodes:", len(self.zero_nodes))
        print("zero lines:", len(self.zero_lines))
        print("lines: ", len(self.lines))
        for i in range(len(self.zero_lines)):
            zero_line = self.zero_lines[i]
            print("zero line", i, "node ids: ", end="")
            for node in zero_line.nodes:
                print(str(node.id) + "-", end ="")
            print()
        
        for i in range(len(self.lines)):
            line = self.lines[i]
            print("line", i, "node ids: ", end="")
            for node in line.nodes:
                print(str(node.id) + "-", end ="")
            print()

        print("no. of triangles:", Triangle.id)


    def get_lines(self):
        # Gets all the zero and nonzero lines in the hatched triangle
        self.get_zero_lines()
        self.get_nonzero_lines()


    def get_nonzero_lines(self):
        """
        Gets all lines that have a starting node on the first zero line
        See (2) in documentation under "Zero lines and zero nodes" and then
        "Generating all lines"
        """

        # Gets all lines that have a start node on the base of a triangle
        # For each node in the first zero line, i.e. base of the triangle
        for root in self.zero_lines[0].nodes:

            # For each node adjacent to root that is not on the zero line,
            # traverse the line defined by (start_node = root, angle)
            for [node, angle] in root.adjacent_nodes:
                if angle != 0:
                    self.traverse(root, angle)

        # Gets all lines that start at the start or end of one of the remaining zero lines
        # For all zero lines except the base of the hatched triangle
        for line in self.zero_lines:
            if line.id != self.zero_lines[0].id:
                self.traverse(line.start_node, 150)
                self.traverse(line.end_node, 30)


    def get_zero_lines(self):
        # For every zero node
        for node in self.zero_nodes:
            self.traverse(node, 0)


    def traverse(self, start_node, angle):
        # creates new line defined by the starting node and angle
        line = Line(start_node, angle)
        reached_end = False
        previous_node = start_node

        # Looks for a node in the previous nodes adjacent nodes that is connected
        # at the same angle (i.e. on the line) that has not already been added to the list,
        # and if there is one adds it, and if there isn't one then we have reached the end
        # of the line, so set the end node.
        while not reached_end:
            line.add_node(previous_node)
            reached_end = True
            for [node, node_angle] in previous_node.adjacent_nodes:
                if node_angle == angle and node.on_line(line) == False:
                    reached_end = False
                    previous_node = node

            if reached_end is True:
                line.set_end_node(previous_node)

        self.lines.append(line)     # Add newly formed lines to lines list
        if angle == 0:              # If zero line, add to zero lines list
            self.zero_lines.append(line)


    def add_new_node(self, triangle):
        # Create a node and add it to the triangle passed in
        node = Node()
        triangle.add_new_node(node)
        self.nodes.append(node)


    def add_flat_triangle(self, layer):
        """
        Adding a flat triangle that is not the first in a layer.
        See documentation Layers, Case 2
        """
        triangle = Triangle(TriangleType.FLAT)
        for i in range(4):
            self.add_new_node(triangle)

        previous_triangle = layer.triangles[len(layer.triangles) - 1]

        node0 = previous_triangle.nodes[0]
        node1 = previous_triangle.nodes[1]
        node4 = previous_triangle.nodes[4]

        triangle.insert_node(0, node0)
        triangle.insert_node(1, node1)
        triangle.insert_node(4, node4)

        triangle.add_edges()

        if len(layer.triangles) == 2 * layer.id:
            self.zero_nodes.append(node0)

        return triangle


    def add_upside_down_triangle(self, i, layer):
        """
        Adding an upside down triangle.
        See documentation Layers, Case 3
        """
        triangle = Triangle(TriangleType.UPSIDE_DOWN)
        for j in range(2):
            self.add_new_node(triangle)

        # see add_bottom_triangle for why previous_layer is at index layer_count - 2

        previous_layer = self.layers[self.layer_count - 2]

        node0 = previous_layer.get_triangle(i - 1).nodes[6]
        node3 = previous_layer.get_triangle(i - 1).nodes[5]

        # previous triangle in the same layer
        previous_triangle = layer.triangles[len(layer.triangles) - 1]

        node4 = previous_triangle.nodes[6]
        node5 = previous_triangle.nodes[3]
        node6 = previous_triangle.nodes[0]

        triangle.insert_node(0, node0)
        triangle.insert_node(3, node3)
        triangle.insert_node(4, node4)
        triangle.insert_node(5, node5)
        triangle.insert_node(6, node6)

        triangle.add_edges()

        return triangle


    def add_bottom_triangle(self):
        # for adding case 1 triangles, see diagrams.png
        """
        For adding the first triangle in a layer
        See documentation, Layers, Case 1
        """
        triangle = Triangle(TriangleType.FLAT)
        for i in range(6):
            self.add_new_node(triangle)
        
        # this would mean it is the first triangle so node 0 is a completely new node
        if self.layer_count == 1:
            self.add_new_node(triangle)
            self.zero_nodes.append(triangle.nodes[0])

        else:
            """
            At this point, self.layers doesnt contain the new layer
            so the previous layer is the last item in the list.
            self.layer_count includes the layer that hasn't been added yet
            so we must subtract 2 rather than 1.
            """

            previous_layer = self.layers[self.layer_count - 2]
            first_triangle = previous_layer.get_triangle(0)
            node = first_triangle.nodes[4]
            triangle.insert_node(0, node)
        
        triangle.add_edges()
        return triangle


    def add_layer(self):
        """See documentation, Layers"""

        layer = Layer()
        self.layer_count += 1

        # The number of triangles in the layer, i.e first layer 1, second 3, third 5, etc
        layer_triangle_count = 2 * self.layer_count - 1

        for i in range(layer_triangle_count):
            # First triangle in the layer, i.e. a bottom triangle
            if i == 0:
                layer.add_triangle(self.add_bottom_triangle())

            # Oddly indexed triangles AKA upside down triangles
            elif i % 2 == 1:
                layer.add_triangle(self.add_upside_down_triangle(i, layer))

            # Evenly indexed triangle
            else:
                layer.add_triangle(self.add_flat_triangle(layer))

        self.layers.append(layer)


    def traverse_line_1(self, root, angle):
        """
        Traverse the first line in the triangle.
        """

        # Find the line that root is on which has the right angle
        for line in root.lines:
            if line.angle == angle:

                # For each non-root unprocessed node on the line,
                # traverse the second line of the triangle
                for node_2 in line.nodes:
                    if not self.is_processed(node_2) and node_2.id != root.id:
                        self.traverse_line_2(root, node_2, angle)

    def traverse_line_2(self, root, node_2, angle):
        # Here angle is specifying the angle of line 1.
        # The second line of the triangle can therefore be any with angle not equal to
        # the angle of the first line, and all fitting this criteria are searched for solutions.
        
        # For all lines coming from node_2 that are not the same as the first line of the triangle
        for line in node_2.lines:
            if line.angle != angle:

                # For all nodes on the second line (excluding node_2)
                for node_3 in line.nodes:
                    if node_3.id != node_2.id:

                        # If the root node (node 1) is connected to node_3 by a straight line,
                        # then a triangle has been found and the solution is to be added.
                        if root.isConnected(node_3) is True:
                            solution = [root, node_2, node_3]
                            self.add_solution(solution)


    def is_processed(self, node):
        # Returns true if the node has already been marked as processed, otherwise false.
        if binary_search(self.processed_node_ids, node.id):
            return True
        return False


    def set_processed(self, node):
        # Mark the node as processed by insorting it to the list of processed node ids.
        insort(self.processed_node_ids, node.id)


    def get_solutions(self):
        """
        See documentation, zero line and zero nodes, generating all lines and finding all triangles.
        """

        # For each zero line
        for line in self.zero_lines:

            # For each zero node on the zero line
            for node_0 in line.nodes:
                if not self.is_processed(node_0):
                    # Most nodes on a zero line will have 2 adjacent nodes with angle 0
                    # Hence here that is seperated from the loop so that the 0 line is 
                    # traversed only once.

                    # Traverse all lines coming from node_0 and search for triangles
                    self.traverse_line_1(node_0, 0)
                    for [node, angle] in node_0.adjacent_nodes:
                        if angle != 0:
                            self.traverse_line_1(node_0, angle)

                # All triangles containing node_0 have now been found, since all lines
                # coming from node_0 have been traversed. Therefore node_0 is marked as 
                # processed, and may be ignored by the triangle finding algorythm.
                self.set_processed(node_0)

        # For all remaining unprocessed nodes
        for line in self.lines:
            for node_0 in line.nodes:
                if not self.is_processed(node_0):

                    # Traverse all lines coming from the node
                    for [node, angle] in node_0.adjacent_nodes:
                        self.traverse_line_1(node_0, angle)

                # All triangles containing node_0 are found so node_0 can be marked as processed
                self.set_processed(node_0)

        # Search the apex which is the last node in self.nodes
        node_0 = self.nodes[len(self.nodes) - 1]
        for [node, angle] in node_0.adjacent_nodes:
            self.traverse_line_1(node_0, angle)


    def add_solution(self, solution):
        """
        Solution ids are the products of the prime ids of the nodes of the triangle.
        These are unique since prime factorisation is unique.
        """
        solution_id = 1
        solution_text = ""
        for i in range(3):
            solution_id *= solution[i].id_prime
            solution_text += str(solution[i].id) + "-"

        solution_text = solution_text[:-1] + "  "
        solution_text += "solution id:" + str(solution_id)

        # Insort from the bisect library adds solution_id to SOLUTION_IDS
        # maintaining SOLUTION_IDS as an ordered list
        if binary_search(SOLUTION_IDS, solution_id) is False:
            insort(SOLUTION_IDS, solution_id)
            if ANALYSE:
                print(solution_text)



def main():
    simulate(36)


def simulate(x):
    start_time = time()
    H = Hatched_Triangle()

    # Add layers
    layer_count = x
    for i in range(layer_count):
        H.add_layer()

    H.get_lines()
    H.get_solutions()

    # Optionally print some data
    if ANALYSE:
        H.analyse()

    # Print solution
    print("T("+ str(layer_count) +") = " + str(len(SOLUTION_IDS)))
    time_taken = time() - start_time
    print("Time taken: ", time_taken)
    H.reset()


if __name__ == "__main__":
    main()