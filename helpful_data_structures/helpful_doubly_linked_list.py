# Define these methods in a specific order
# to minimize the amount of code you need to write
# The order is mentioned above each method in the form of "Order num)"
# Order and implementation from: https://www.algoexpert.io/questions/Linked%20List%20Construction

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    # Obviously define this before anything
    def __init__(self):
        self.head = None
        self.tail = None

    # Order 7)
    # O(k) time | O(k) space
    def setHead(self, node):

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.insertBefore(self.head, node)

    # Order 8)
    # O(k) time | O(k) space
    def setTail(self, node):

        if self.tail is None:
            self.head = node
            self.tail = node
            return

        self.insertAfter(self.tail, node)

    # Order 5)
    # O(k) time | O(k) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return None
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # Order 6)
    # O(k) time | O(k) space
    def insertAfter(self, node, nodeToInsert):

        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return None
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # Order 9)
    # O(p) time | O(k) space
    def insertAtPosition(self, position, nodeToInsert):

        if position == 1:
            self.setHead(nodeToInsert)
            return

        node = self.head
        currPosition = 1

        while node is not None and currPosition != position:
            node = node.next
            currPosition += 1

        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    # Order 4)
    # O(n) time | O(k) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # Order 2)
    # O(k) time | O(k) space
    def remove(self, node):

        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # Order 1)
    # O(n) time | O(k) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            return False
        else:
            return True

    # Order 3)
    def removeNodeBindings(self, node):

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def __iter__(self):
        cursor = self.head.next
        while(cursor is not self.tail):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"











