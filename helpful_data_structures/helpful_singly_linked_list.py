class SinglyLinkedList:
    class Node:
        def __init__(self, val=None):
            self.data = val
            self.next = None

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.head = SinglyLinkedList.Node()
        self.size = 0

        self.last = self.head

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):
        new_node = SinglyLinkedList.Node(val)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
        return new_node

    def add_first(self, val):
        node = self.add_first(self.head, val)
        if (len(self) == 1):
            self.last = node
        return node

    def add_last(self, val):
        self.last = self.add_after(self.last, val)
        return self.last

    def add_before(self, node, val):
        curr = self.head
        while curr.next is not node:
            curr = curr.next

        new_node = SinglyLinkedList.Node(val)
        curr.next = new_node

        new_node.next = node

        self.size += 1
        return new_node

    def delete_node(self, node):
        curr = self.head

        while curr.next is not node:
            curr = curr.next

        curr.next = node.next
        self.size -= 1

        val = node.data
        node.disconnect()
        return val

    def delete_first(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.head.next)

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")

        curr = self.head
        while curr.next is not self.last:
            curr = curr.next

        val = self.delete_node(self.last)
        self.last = curr
        return val

    def __iter__(self):
        cursor = self.head.next
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + ' --> '.join([str(elem) for elem in self]) + "]"






