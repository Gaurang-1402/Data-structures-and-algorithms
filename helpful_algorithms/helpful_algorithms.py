
    # pointer2 = 0
    #
    # while lst[pointer1] >= pivot:
    #
    #

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
# main()

# ///////////////////////////////////////////////

# Values in range algorithm

def find_duplicates(lst):

    len_list = len(lst)

    duplicate_lst = []
    for i in range(len(lst)):

        #Since the values of lst are in the range of len lst
        #associate position of elements in lst with the values in lst
        #Because the given values in lst will not cross len(lst)
        #I'm adding len(lst)
        #The % operator is used to get back the original index of the list

        lst[lst[i] % len_list] = lst[lst[i] % len_list] + len_list

    for i in range(len(lst)):
        if lst[i] > (2 * len_list):
            duplicate_lst.append(i)

    return duplicate_lst

def main():
    duplicates_lst = find_duplicates([2, 3, 4, 3, 3, 3, 2])

    print(duplicates_lst)

# ///////////////////////////////////////////////

# Generator function

def factors(num):
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            yield i

    for i in range(int(num ** 0.5) - 1, 0, -1):
        if num % i == 0:
            yield num // i

def main():
    for curr_factor in factors(100):
        print(curr_factor, end=' ')



# ///////////////////////////////////////////////

# Binary search

# MUST BE SORTED AND THETA(logn) runtime

def binary_search(lst, val):

    low = 0
    high = len(lst) - 1

    while high > low:
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


# ///////////////////////////////////////////////

# Recursive with helper

def count_appearances2(lst, val):
    def count_appearances_helper(lst, low, high, val):
        if (low == high):
            if (lst[low] == val):
                return 1
            else:
                return 0
        else:
            count_rest = count_appearances_helper(lst, low + 1, high, val)
            if (lst[low] == val):
                return count_rest + 1
            else:
                return count_rest

    if(len(lst) == 0):
        return 0
    else:
        return count_appearances_helper(lst, 0, len(lst) - 1, val)

# Recursion with log(n) runtime

def power(a, n):

    if n==1:
        return a
    else:
        res = power(a, n-1)
        res *= a
    return res

def fast_power(a, n):

    if n==1:
        return a
    else:
        part = fast_power(a, n // 2)
        if (n % 2 == 0):
            return part * part
        else:
            return a * part * part

print(fast_power(2, 5))

# ///////////////////////////////////////////////

# Array type

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter_collection = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

        if (iter_collection):
            for elem in iter_collection:
                self.append(elem)

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        if ind < 0:
            return self.data_arr[ind + self.n]

        else:
            return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if ind < 0:
            self.data_arr[ind + self.n] = val

        else:
            self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        string_list = self.n * [None]
        for i in range(self.n):

            string_list[i]= str(self[i])

        return "[" + ", ".join(string_list) + "]"

    def __add__(self, other):
        new_array = ArrayList()
        new_array.extend(self)
        new_array.extend(other)
        return new_array

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, scalar):
        lst = ArrayList()
        for i in range(scalar):
            lst.extend(self)

        return lst

    def __rmul__(self, scalar):
        return self * scalar

    def remove(self, val):
        if val in self:
            data = make_array(self.capacity)

        i = 0
        while self[i] != val:
            data[i] = self[i]
            i = i + 1
        while (i + 1) < self.n:
            data[i] = self[i + 1]
            i += 1
        self.data = data
        self.n = self.n - 1

    def removeAll(self, val):
        count = 0
        for num in self:
            if num == val:
                count += 1
        data = make_array(self.capacity)

        index = 0

        for num in self:
            if num != val:
                data[index] = num
                index += 1

        self.data = data
        self.n = self.n - count

    def insert(self, index, val):
        if (not (-self.n <= index < self.n)):
            raise IndexError('Invalid index')

        if index < 0:
            index = self.n + index

        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        data = make_array(self.capacity)
        i = 0
        while i != index:
            data[i] = self[i]
            i = i + 1
        data[i] = val
        i = i + 1
        while i <= self.n:
            data[i] = self[i-1]
            i += 1

        self.data_arr = data
        self.n = self.n + 1

    def pop(self, index=None):
        if index != None:
            if index < 0:
                index = self.n + index
            if (not (-self.n <= index <= self.n - 1)):
                raise IndexError('Invalid index')
            else:
                i = 0
                data = make_array(self.capacity)

                while i != index:
                    data[i] = self[i]
                    i = i + 1
                last_num = self[i]

                while i < (self.n - 1):
                    data[i] = self[i+1]
                    i += 1
                self.data_arr = data
                self.n = self.n - 1

        else:
            last_num = self[-1]
            self[-1] = None
            self.n = self.n - 1

        if self.n < (self.capacity//4):
            self.resize(int(0.5 * self.capacity))

        return last_num
