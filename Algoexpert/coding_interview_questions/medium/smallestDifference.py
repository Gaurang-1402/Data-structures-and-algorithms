def smallestDifference(arrayOne, arrayTwo):
    curr_min_diff = abs(arrayTwo[0] - arrayOne[0])

    final_lst = []

    for i in range(len(arrayOne)):
        num_1 = arrayOne[i]
        for j in range(len(arrayTwo)):
            num_2 = arrayTwo[j]
            check_diff = abs(num_1 - num_2)
            if check_diff < curr_min_diff:
                curr_min_diff = check_diff
                final_lst = [num_1, num_2]


    return final_lst






def main():
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]


    diff_arr = smallestDifference(arrayOne, arrayTwo)

    print(diff_arr)

main()
