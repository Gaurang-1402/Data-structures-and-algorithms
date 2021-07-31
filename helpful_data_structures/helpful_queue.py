import ctypes  # provides low-level arrays

# THIS IS A FIXED SIZED QUEUE- ALSO KNOWN AS sQ: Static Queue

def make_array(n):
    return (n * ctypes.py_object)()

class ArrayQueue:

    initial_capacity = 10

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.initial_capacity) #len(self.data_arr) = 10
        self.num_of_items = 0
        self.front_ind = None
        self.print_list = []

    def __len__(self): # theta(1)
        return self.num_of_items


    def is_empty(self): # theta(1)
        #return self.num_of_items == 0
        return len(self) == 0


# =============================================================================
#     def resize(self, new_size):
#         new_array = make_array(new_size)
#         for i in range(self.n):
#             new_array[i] = self.data[i]
#         self.data = new_array
#         self.capacity = new_size
#
# =============================================================================

    def __repr__(self):
        print("Real Queue doesn't look like this it may have front and back index somewhere in the middle and Nones in the capacity")
        return "[|sQ| "+", ".join([str(elem) for elem in self.print_list]) + " |sQ|]"


    def enqueue(self, item): # theta(1)
        if len(self) == len(self.data_arr):      #ArrayQueue.initial_capacity:
            raise Exception("Fixed_Sized_Queue is Full")
            #self.resize(2*len(self.data_arr))

        if self.is_empty():
            self.data_arr[0] = item
            self.num_of_items += 1
            self.front_ind = 0
        else:
            end_ind = (self.front_ind + self.num_of_items) % len(self.data_arr) #ArrayQueue.initial_capacity
            # circular construction
            self.data_arr[end_ind] = item
            self.num_of_items += 1
        self.print_list.append(item)


    def dequeue(self): # theta(1)
        if self.is_empty():
            raise Exception("Queue is Empty!!!")

        return_value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind+1)%len(self.data_arr) #ArrayQueue.initial_capacity
        self.num_of_items -= 1

        if self.is_empty():
            self.front_ind = None

        self.print_list.pop(0)

        return return_value


    def first(self): # theta(1)
        if self.is_empty():
            raise Exception("Queue is Empty!!!")

        return self.data_arr[self.front_ind]

# Q = ArrayQueue()
# for i in range(10):
#     Q.enqueue(i+10)
# print(Q)
# print(Q.is_empty())

