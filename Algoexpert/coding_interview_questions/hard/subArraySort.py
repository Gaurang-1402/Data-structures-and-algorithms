def subArraySort(array):

    final_lst = []

    new_lst = []

    for i in range(len(array)-1):
        curr_num = array[i]
        next_num = array[i+1]



        if curr_num <= next_num:
            new_lst.append(curr_num)
        else:
            new_lst.append(curr_num)
            new_lst.append(next_num)
            trav = i
            high = i
            if next_num==6:
                print(new_lst)
                print(new_lst[trav])
                print(new_lst[trav+1])

            while new_lst[trav + 1] < new_lst[trav]:
                if next_num==6:
                    print(new_lst[trav+1])
                new_lst[trav+1], new_lst[trav] = new_lst[trav], new_lst[trav+1]
                trav = trav - 1

            low = trav

    return [low, high]


    print(new_lst)






def main():
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]



    sort_arr = subArraySort(array)

    print(sort_arr)

main()
