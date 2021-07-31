# Solution #1
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#
# 	sum_lst = []
#
# 	for pointer1 in range(len(array)):
# 		for pointer2 in range(len(array)):
# 			if pointer1 == pointer2:
# 				continue
#             if array[pointer2] in sum_lst:
#                 continue
#
# 			if (array[pointer1] + array[pointer2]) == targetSum:
# 				sum_lst.append(array[pointer1])
# 				sum_lst.append(array[pointer2])
#
#
#
# 	return sum_lst


# Solution #2


# WHAT I DID

# def twoNumberSum(array, targetSum):
#     # Write your code here.
#
# 	sum_lst = []
#
# 	for pointer1 in range(len(array)):
# 		for pointer2 in range(len(array)):
# 			if pointer1 == pointer2:
# 				continue
#             if array[pointer2] in sum_lst:
#                 continue
#
# 			if (array[pointer1] + array[pointer2]) == targetSum:
# 				sum_lst.append(array[pointer1])
# 				sum_lst.append(array[pointer2])
#
#
#
# 	return sum_lst
#
#
# print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
