class StackArr:
    def __init__(self, size):
        self.items = [None for _ in range(size)]
        self.top = -1

    def push(self, data):
        if self.top + 1 == len(self.items):
            print("stack overflow")
            print("increasing size...")
            new_items = [None for _ in range(len(self.items))]
            self.items += new_items

        self.top += 1
        self.items[self.top] = data

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        else:
            data = self.items[self.top]
            self.top -= 1
            return data



    def __len__(self):
        return self.top + 1

def peek(stack):
    if stack.top == -1:
        raise IndexError("empty stack")
    else:
        return stack.items[stack.top]
my_stack = StackArr(3)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.pop())
print(my_stack.pop())
print(peek(my_stack))
print(my_stack.pop())
print(my_stack.pop())