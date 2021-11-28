# This is Depth-first search
# Breadth-first search is available in helpful_data_structures/helpful_binary_search.py
# scroll till down
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):

        if self.children == []:

            return array
        else:
            if self.name not in array:
                array.append(self.name)
            for child in self.children:
                array.append(child.name)
                child.depthFirstSearch(array)

            return array
