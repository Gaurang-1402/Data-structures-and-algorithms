# SELECTION SORT

def selection_sort(lst, n):
    #    lst = [5, 14, 10, 8, 13, 1, 18, 3, 4, 2, 19, 3, 4]
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    # Time Complexity: O(n2) as there are two nested loops.


def insertion_sort(lst, n):
    for i in range(n):
        curr = lst[i]  # 5 14 10
        j = i  # 0 1 2

        while (j >= 1) and curr < lst[j - 1]:
            # curr --> 10
            # lst[j-1] --> 14
            lst[j] = lst[j - 1]
            j = j - 1

        lst[j] = curr


def bubble_sort(lst, n):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


def quick_sort(lst):
    if len(lst) < 1:
        return lst
    else:
        pivot = lst.pop()
        less_than_lst = []
        greater_than_equal_to_lst = []

        for elem in lst:
            if elem >= pivot:
                greater_than_equal_to_lst.append(elem)
            else:
                less_than_lst.append(elem)

        return quick_sort(less_than_lst) + [pivot] + quick_sort(greater_than_equal_to_lst)


def quickselect(array, k):

    def quick_select_helper(lst, low, high, k):
        # Worst-case performance: О(n2)
        # Best-case performance: (n)
        # Data structure: Array
        # Class: Selection algorithm

        pivot = partition(lst, low, high)

        if pivot == k - 1:
            return lst[pivot]
        elif pivot < k - 1:
            return quick_select_helper(lst, pivot + 1, high, k)
        elif pivot > k - 1:
            return quick_select_helper(lst, low, pivot - 1, k)

    def partition(lst, low, high):
        i = low - 1
        pivot = lst[high]

        for j in range(low, high):
            if lst[j] <= pivot:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]

        return (i + 1)

    # MAIN CALL
    return quick_select_helper(array, 0, len(array) - 1, k)


def main():
    lst = [5, 14, 10, 8, 13, 1, 18, 3, 4, 2, 19, 3, 4]
    # selection_sort(lst, len(lst))
    # insertion_sort(lst, len(lst))

    sorted_lst = quick_sort(lst)

    for elem in sorted_lst:
        print(elem, end=' ')


main()
