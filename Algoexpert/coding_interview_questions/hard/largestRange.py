def largestRange(array):
    array.sort()


    final_lst = []
    temp_lst = []
    curr_i = 0
    next_i = 1
    next_num = array[next_i]

    while curr_i < len(array):
        curr_num = array[curr_i]
        if len(temp_lst) == 0:
            temp_lst.append(curr_num)
        if curr_num + 1 == next_num:
            temp_lst.append(next_num)
        elif curr_num == next_num:
            temp_lst.append(next_num)
        else:
            final_lst.append(temp_lst)
            temp_lst = []
        curr_i = curr_i + 1
        next_i = next_i + 1
        if curr_i < len(array) - 1:
            next_num = array[next_i]
    final_lst.append(temp_lst)
    print(final_lst)

    max_diff = float('-inf')

    for lst in final_lst:
        if (lst[-1] - lst[0]) > max_diff:
            max_diff = lst[-1] - lst[0]
            curr_lst = [lst[0], lst[-1]]

    return curr_lst

# def largestRange(array):
#     # Write your code here.
#     checker_map = {}
# 	temp_lst = []
# 	final_lst = []
#
# 	for num in array:
# 		if num not in checker_map:
# 			checker_map[num] = False
#
# 	for i in range(len(array)):
# 		begin_num = array[i]
# 		if checker_map[begin_num] == True:
# 			continue
# 		curr_low = begin_num
# 		while curr_low - 1 in checker_map:
# 			checker_map[curr_low - 1] = True
# 			temp_lst.append(curr_low-1)
# 			curr_low = curr_low - 1
#
#
# 		temp_lst.append(begin_num)
#
# 		curr_high = begin_num
# 		while curr_high + 1 in checker_map:
# 			checker_map[curr_high + 1] = True
# 			temp_lst.append(curr_high+1)
# 			curr_high = curr_high + 1
#
# 		final_lst.append(temp_lst)
# 		temp_lst = []
# 	print(final_lst)
#
#     max_diff = float('-inf')
#
#
# 	for lst in final_lst:
#         if (lst[-1] - lst[0]) > max_diff:
#             max_diff = lst[-1] - lst[0]
#             curr_lst = [lst[0], lst[-1]]
#
#
#     return curr_lst
def main():
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

    ans = largestRange(array)
    print(ans)


main()
