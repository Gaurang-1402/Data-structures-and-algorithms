

# Pointer 1 & 2

def split_parity(lst):

     even_pointer = 0

     for odd_pointer in range(len(lst)):
         if lst[odd_pointer] % 2 != 0:
             # I know that lst[odd_pointer] is an odd element
             lst[odd_pointer], lst[even_pointer] = lst[even_pointer], lst[odd_pointer]
             even_pointer += 1
def main():
    original_lst = [2, 4, 6, 8, 10, 11]
    split_parity(original_lst)


    print(original_lst)
main()
