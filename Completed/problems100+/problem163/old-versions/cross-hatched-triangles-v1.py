import sys, os
sys.path.append(os.path.abspath(r"C:\Users\Dell\Desktop\code\Python\project-euler"))
from helpers import *
from bisect import insort

# version 1
# It works! But it is far too slow...

PRIMES = get_N_primes(3997)
PATH_IDS = []

class Node:
    id = 0

    def __init__(self):
        # elements in adjacent_nodes are as such: [node, angle]
        self.id = Node.id
        self.id_prime = PRIMES[self.id]
        Node.id += 1
        self.adjacent_nodes = []


    def add_adjacent(self, node, angle):
        self.adjacent_nodes.append([node, angle])


class Triangle:
    id = 0

    def __init__(self, type):
        # type in ["FLAT","UPSIDE_DOWN"]
        self.id = Triangle.id
        Triangle.id += 1

        #self.edges might be unneccessary...
        self.edges = []
        self.nodes = []
        self.type = type


    def add_edge(self, index1, index2, angle):
        # upside down triangles are essentially normal triangles that have been reflected
        # horizontally, in the sense that their nodes are numbered in this way
        # as such, the angles are equal to 180 - angle (mod 180)
        # see diagrams.png

        node1, node2 = self.nodes[index1], self.nodes[index2]
        if self.type == "UPSIDE_DOWN":
            angle = (180 - angle) % 180
        node1.add_adjacent(node2, angle)
        node2.add_adjacent(node1, angle)


    def add_edges(self):
        # connects all nodes that should be connected together with their respective angles
        # note: add_edge handles the angle adjustment for upside down triangles
        # see diagrams.png
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
        self.nodes.append(node)


    def insert_node(self, index, node):
        self.nodes.insert(index, node)


class Layer:
    id = 0
    
    def __init__(self):
        self.id = Layer.id
        Layer.id += 1
        self.triangles = []

    
    def get_triangle(self,index):
        return self.triangles[index]


    def add_triangle(self,triangle):
        self.triangles.append(triangle)


class Edge:
    id = 0

    def __init__(self):
        self.id = Edge.id
        Edge.id += 1


class Path:
    def __init__(self, root):
        # root is the root node, the node from which the path starts (and ends)
        # angle[i] is the angle of the edge from node self.path[i-1] to self.path[i]
        #   or self.root to self.path[0] when i = 0
        self.root = root
        self.path = []
        self.angles = []
        self.sides = 0
        self.current_direction = None


    def remove_node(self):
        # removes node at the end of the path, along with the angle in self.angles
        # updates sides and current_direction

        length = len(self.path)
        if length == 0:
            return False

        elif length == 1:
            self.sides = 0
            self.current_direction = None

        else:
            if self.angles[length - 2] != self.angles[length - 1]:
                self.current_direction = self.angles[length - 2]
                self.sides -= 1

        self.path.pop()
        self.angles.pop()

        return True


    def add_node(self, node, angle):
        self.path.append(node)
        self.angles.append(angle)
        if self.current_direction != angle:
            self.current_direction = angle
            self.sides += 1
            

    def isValid(self, next_node_list):
        # returns two booleans 
        # first is if the next node will make a valid path or not
        # second is if the next node will complete a triangle
        direction_change = False

        # checks that next node is not already in path, (does not check root)
        for node in self.path:
            if next_node_list[0].id == node.id:
                return False, False

        # then this means a change of direction, starting a new side of triangle
        if next_node_list[1] != self.current_direction:
            direction_change = True

            # if self.sides is 3 and the next node would change direction then
            # this would give us 4 sides, i.e. path is invalid
            if self.sides == 3:
                return False, False

        # checks that the next node is the root node and has completed a triangle
        if next_node_list[0].id == self.root.id:
            if (self.sides == 3 and not direction_change) or (self.sides == 2 and direction_change):
                return True, True

            else:
                return False, False

        return True, False


    def get_id(self):
        # root node is always the last in self.path at this point
        # so no need to multiply product by self.root.id_prime
        product = 1
        for node in self.path:
            product *= node.id_prime

        return product

    
    def __str__(self):
        line = str(self.root.id) + "-"
        for node in self.path:
            line += str(node.id) + "-"
        line = line[:-1]
        return line
    

    def get_next_node(self, index):
        # return node, angle if successful
        # otherwise return False

        if self.path:
            node = self.path[len(self.path) - 1]
        else:
            node = self.root

        try:
            return node.adjacent_nodes[index]

        except IndexError:
            return False



class Hatched_Triangle:
    def __init__(self):
        self.layers = []
        self.nodes = []
        self.layer_count = 0


    def add_new_node(self, triangle):
        node = Node()
        triangle.add_new_node(node)
        self.nodes.append(node)


    def add_flat_triangle(self, layer):
        triangle = Triangle("FLAT")
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

        return triangle


    def add_upside_down_triangle(self, i, layer):
        triangle = Triangle("UPSIDE_DOWN")
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
        triangle = Triangle("FLAT")
        for i in range(6):
            self.add_new_node(triangle)
        
        # this would mean it is the first triangle so node 0 is a completely new node
        if self.layer_count == 1:
            self.add_new_node(triangle)

        else:
            # at this point, self.layers doesnt contain the new layer
            # so the previous layer is the last item in the list
            # self.layer_count includes the layer that hasn't been added yet
            # so we must subtract 2 rather than 1

            previous_layer = self.layers[self.layer_count - 2]
            first_triangle = previous_layer.get_triangle(0)
            node = first_triangle.nodes[4]
            triangle.insert_node(4, node)
        
        triangle.add_edges()
        return triangle


    def add_layer(self):
        layer = Layer()
        self.layer_count += 1

        # the number of triangles in the layer, i.e first layer 1, second 3, third 5, etc
        layer_triangle_count = 2 * self.layer_count - 1

        for i in range(layer_triangle_count):
            # first triangle in the layer, i.e. a bottom triangle
            if i == 0:
                layer.add_triangle(self.add_bottom_triangle())

            # odd index triangles AKA upside down triangles
            elif i % 2 == 1:
                layer.add_triangle(self.add_upside_down_triangle(i, layer))

            # even index triangle
            else:
                layer.add_triangle(self.add_flat_triangle(layer))

        self.layers.append(layer)

    
    def get_solutions(self):
        for node in self.nodes:
            path = Path(node)
            indexes = [0]
            pointer = 0
            keepGoing = True

            while keepGoing:
                # node, angle
                next_node_list = path.get_next_node(indexes[pointer])
                
                # IndexError meaning that we must now go back one in the path
                if next_node_list is False:
                    pointer -= 1
                    indexes[pointer] += 1
                    indexes.pop()
                    path.remove_node()

                    if pointer == -1:
                        keepGoing = False
                        break
                    
                else:
                    valid_path, triangle_completed = path.isValid(next_node_list)

                    # if path is otherwise valid but not for index error then we choose the 
                    # next option at the current location by incrementing the index
                    if valid_path is False:
                        indexes[pointer] += 1

                    # next_node completes a valid triangle
                    elif triangle_completed is True:
                        path.add_node(next_node_list[0], next_node_list[1])
                        path_id = path.get_id()

                        # insort from the bisect library adds path_id to PATH_IDS
                        # maintaining PATH_IDS as an ordered list
                        if binary_search(PATH_IDS, path_id, 0, len(PATH_IDS) - 1) is False:
                            insort(PATH_IDS, path_id)

                        path.remove_node()

                        indexes[pointer] += 1

                    # path is valid but doesn't make a triangle
                    else:
                        path.add_node(next_node_list[0], next_node_list[1])
                        indexes.append(0)
                        pointer += 1


def main():
    H = Hatched_Triangle()
    for i in range(2):
        H.add_layer()

    H.get_solutions()
    print(len(PATH_IDS))


if __name__ == "__main__":
    main()