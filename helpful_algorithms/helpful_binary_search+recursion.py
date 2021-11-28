
# Binary search

# MUST BE SORTED AND THETA(logn) runtime

def binary_search(lst, val):

    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (high + low) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            high = mid - 1
        elif lst[mid] < val:
            low = mid + 1

    return "Value not present"

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

search_idx = binary_search(lst, 8)

print(search_idx)


print(binary_search([2, 3, 5, 6, 3, 5, 2, 8, 9], 9))



#Binary search with recursion

def recursion_binary_search(srt_lst, low, high, val):
    if low>high:
        return None
    else:
        mid = (high + low) // 2
        if srt_lst[mid] == val:
            return mid
        elif srt_lst[mid] > val:
            ind = recursion_binary_search(srt_lst, low, mid - 1, val)

        elif srt_lst[mid] < val:
            ind = recursion_binary_search(srt_lst, mid + 1, high, val)

        return ind
def main():
    print(recursion_binary_search([1, 2, 4, 5, 6, 7, 8, 4], 0, 7, 6))

main()

