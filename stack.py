from DoublyLinkedList import DoublyLinkedList

class Stack:
    def __init__(self):
        self.items = DoublyLinkedList()

    def push(self, data):
        self.items.append(data)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Stack underflow")

    def top(self):
        return self.items.tail.data

    def size(self):
        return len(self.items)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.top())
print(my_stack.pop())
print(my_stack.pop())
#print(my_stack.pop())



