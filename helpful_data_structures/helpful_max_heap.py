# currentNode = i
# childOne = 2i + 1
# childTwo = 2i + 2
# parentNode = (i - 1) // 2

class MaxHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)
        self.length = len(array)

    def buildHeap(self, array):
        firstParentIdx = len(array) - 2 // 2
        for currParentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currParentIdx, len(array) - 1, array)
        return array

    def isEmpty(self):
        return len(self.heap) == 0

    def getLength(self):
        return len(self.heap)

    def siftDown(self, currIdx, endIdx, heap):
        childOneIdx = 2 * currIdx + 1
        while childOneIdx <= endIdx:
            # childTwoIdx
            if 2 * currIdx + 2 <= endIdx:
                childTwoIdx = 2 * currIdx + 2
            else:
                childTwoIdx = -1

            if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] > heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                childOneIdx = 2 * currIdx + 1
            else:
                return

    def siftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] > heap[parentIdx]:
            self.swap(currIdx, parentIdx, self.heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2


    def insert(self, val):
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valToBeRemoved = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valToBeRemoved

    def peek(self):
        return self.heap[0]

    def swap(self, currIdx, swapIdx, heap):
        heap[currIdx], heap[swapIdx] = heap[swapIdx], heap[currIdx]








#
#
# import sys
# class MaxHeap:
#
#     def __init__(self, maxsize):
#
#         self.maxsize = maxsize
#         self.size = 0
#         self.Heap = [0] * (self.maxsize + 1)
#         self.Heap[0] = sys.maxsize
#         self.FRONT = 1
#
#     # Function to return the position of
#     # parent for the node currently
#     # at pos
#     def parent(self, pos):
#
#         return pos // 2
#
#     # Function to return the position of
#     # the left child for the node currently
#     # at pos
#     def leftChild(self, pos):
#         return 2 * pos
#
#     # Function to return the position of
#     # the right child for the node currently
#     # at pos
#     def rightChild(self, pos):
#
#         return (2 * pos) + 1
#
#     # Function that returns true if the passed
#     # node is a leaf node
#     def isLeaf(self, pos):
#
#         if pos >= (self.size//2) and pos <= self.size:
#             return True
#         return False
#
#     # Function to swap two nodes of the heap
#     def swap(self, fpos, spos):
#
#         self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
#                                             self.Heap[fpos])
#
#     # Function to heapify the node at pos
#     def maxHeapify(self, pos):
#
#         # If the node is a non-leaf node and smaller
#         # than any of its child
#         if not self.isLeaf(pos):
#             if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
#                 self.Heap[pos] < self.Heap[self.rightChild(pos)]):
#
#                 # Swap with the left child and heapify
#                 # the left child
#                 if (self.Heap[self.leftChild(pos)] >
#                     self.Heap[self.rightChild(pos)]):
#                     self.swap(pos, self.leftChild(pos))
#                     self.maxHeapify(self.leftChild(pos))
#
#                 # Swap with the right child and heapify
#                 # the right child
#                 else:
#                     self.swap(pos, self.rightChild(pos))
#                     self.maxHeapify(self.rightChild(pos))
#
#     # Function to insert a node into the heap
#     def insert(self, element):
#
#         if self.size >= self.maxsize:
#             return
#         self.size += 1
#         self.Heap[self.size] = element
#
#         current = self.size
#
#         while (self.Heap[current] >
#                self.Heap[self.parent(current)]):
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
#
#     # Function to print the contents of the heap
#     def Print(self):
#
#         for i in range(1, (self.size // 2) + 1):
#             print(" PARENT : " + str(self.Heap[i]) +
#                   " LEFT CHILD : " + str(self.Heap[2 * i]) +
#                   " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
#
#     # Function to remove and return the maximum
#     # element from the heap
#     def extractMax(self):
#
#         popped = self.Heap[self.FRONT]
#         self.Heap[self.FRONT] = self.Heap[self.size]
#         self.size -= 1
#         self.maxHeapify(self.FRONT)
#
#         return popped
#
# # Driver Code
# if __name__ == "__main__":
#
#     print('The maxHeap is ')
#
#     maxHeap = MaxHeap(15)
#     maxHeap.insert(5)
#     maxHeap.insert(3)
#     maxHeap.insert(17)
#     maxHeap.insert(10)
#     maxHeap.insert(84)
#     maxHeap.insert(19)
#     maxHeap.insert(6)
#     maxHeap.insert(22)
#     maxHeap.insert(9)
#
#     maxHeap.Print()
#
#     print("The Max val is " + str(maxHeap.extractMax()))
