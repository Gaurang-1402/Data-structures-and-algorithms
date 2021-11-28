# currentNode = i
# childOne = 2i + 1
# childTwo = 2i + 2
# parentNode = (i - 1) // 2

class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)
		self.length = len(array)

	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currIdx, len(array) - 1, array)
		return array

	def getLength(self):
		return len(self.heap)

	def isEmpty(self):
		return len(self.heap) == 0

	def siftDown(self, currIdx, endIdx, heap):
		childOneIdx = currIdx * 2 + 1

		while childOneIdx <= endIdx:
			if currIdx * 2 + 2 <= endIdx:
				childTwoIdx = currIdx * 2 + 2
			else:
				childTwoIdx = -1

			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx

			if heap[idxToSwap] < heap[currIdx]:
				self.swap(currIdx, idxToSwap, heap)
				currIdx = idxToSwap
				childOneIdx = currIdx * 2 + 1

			else:
				return

	def siftUp(self, currIdx, heap):
		parentIdx = (currIdx - 1)//2
		while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
			self.swap(currIdx, parentIdx, heap)
			currIdx = parentIdx
			parentIdx = (currIdx - 1) // 2

	def peek(self):
		return self.heap[0]

	def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]




