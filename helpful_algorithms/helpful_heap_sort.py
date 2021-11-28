# Best: O(nlog(n)) time | O(1) space
# Average: O(nlog(n)) time | O(1) space
# Worst: O(nlog(n)) time | O(1) space
def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)

    return array

def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currIdx, len(array) - 1, array)

def siftDown(currIdx, endIdx, heap):
    childOneIdx = currIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currIdx * 2 +2 if currIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currIdx]:
            swap(currIdx, idxToSwap, heap)
            currIdx = idxToSwap
            childOneIdx = currIdx * 2 + 1
        else:
            return None

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]




