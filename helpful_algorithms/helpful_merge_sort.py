def merge_sort(lst):
    #the return values don't matter we only need to mutate the list
    if (len(lst) == 0):
        return lst
    elif (len(lst) == 1):
        return lst
    else:
        mid = (len(lst)) // 2
        left_lst = lst[ : mid]
        right_lst = lst[mid : ]
        merge_sort(left_lst)
        merge_sort(right_lst)
        merged = merge(left_lst, right_lst)
        for i in range(len(merged)):
            lst[i] = merged[i]
        return lst

def merge(srt_lst1, srt_lst2):

    merged_list = []
    i1 = 0
    i2 = 0
    while ((i1 < len(srt_lst1)) and (i2 < len(srt_lst2))):
        if (srt_lst1[i1] < srt_lst2[i2]):
            merged_list.append(srt_lst1[i1])
            i1 += 1
        else:
            merged_list.append(srt_lst2[i2])
            i2 += 1
    while (i1 < len(srt_lst1)):
        merged_list.append(srt_lst1[i1])
        i1 += 1
    while (i2 < len(srt_lst2)):
        merged_list.append(srt_lst2[i2])
        i2 += 1
    return merged_list

def main():
    lst = [5, 14, 10, 8, 13, 1, 18, 3, 4, 2, 19, 3, 4]
    merge_sort(lst)

    for elem in lst:
        print(elem, end=' ')

main()
