

# Pointer 1 & 2

def split_parity(lst):

     last_odd = 0

     for i in range(len(lst)):
         if lst[i] % 2 != 0:
             # I know that lst[i] is an odd element
             lst[i], lst[last_odd] = lst[last_odd], lst[i]
             last_odd += 1
def main():
    original_lst = [2, 4, 6, 8, 10, 11]
    split_parity(original_lst)


    print(original_lst)
