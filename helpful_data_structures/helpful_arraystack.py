from helpful_data_structures.helpful_arraylist import ArrayList
class ArrayStack:

    def __init__(self):
        self.data = ArrayList()
        self.print_list = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.data.append(item)
        self.print_list.append(item)

    def __repr__(self):
        return "[|s| "+", ".join([str(elem) for elem in self.print_list]) + " |s|]"

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!!!")
        self.print_list.pop()

        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!!!")

        return self.data[-1]

def main():
    s = ArrayStack()
    s.push(2)
    s.push(3)
    print(s)
# main()
