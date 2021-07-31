# Binary search type with application

#Not theta(logn) but theta(n) runtime

def two_sum(srt_lst, target):

    low = 0
    high = len(srt_lst) - 1

    while high > low:

        if srt_lst[high] + srt_lst[low] == target:
            return high, low

        elif srt_lst[high] + srt_lst[low] > target:
            high = high - 1

        elif srt_lst[high] + srt_lst[low] < target:
            low = low + 1

    return srt_lst

def main():
    sum_index_tuple = two_sum([-2, 7, 11, 15, 20, 21], 19)

    print(sum_index_tuple)
