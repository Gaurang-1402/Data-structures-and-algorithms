
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
