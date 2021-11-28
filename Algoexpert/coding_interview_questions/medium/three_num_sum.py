

def threeNumberSum(array, targetSum):

    final_lst = []

    array.sort()

    for i in range(len(array) - 2):

        low = i + 1
        high = len(array) - 1

        while high > low:

            low_num = array[low]
            mid_num = array[i]
            high_num = array[high]

            if (low_num + mid_num + high_num) == targetSum:
                final_lst.append([low_num, mid_num, high_num])
                low = low + 1
                high = high - 1
            elif (low_num + mid_num + high_num) > targetSum:
                high = high - 1
            elif (low_num + mid_num + high_num) < targetSum:
                low = low + 1


    return final_lst

    # nums = {}
    #
    # final_lst = []
    # temp_lst=[]
    #
    # for i in range(len(array)):
    #     num_1 = array[i]
    #     for j in range(len(array)):
    #         num_2 = array[j]
    #         if i == j:
    #             continue
    #         potential_match = targetSum - num_1 - num_2
    #         if potential_match in nums:
    #             final_lst.append([num_1, num_2, potential_match])
    #         else:
    #             nums[num_1] = True
    #
    # return final_lst






def main():
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0

    final_lst = threeNumberSum(array, targetSum)
    print(final_lst)

main()
